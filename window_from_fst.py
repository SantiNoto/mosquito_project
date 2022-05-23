import pandas as pd

def window_build_no_overlap(source_file, target_file, window_size = 80):
    df_t = pd.read_csv(source_file,delimiter='\t')
    # extract non overlaping windows
    df = pd.DataFrame(columns=['window.pos'])
    start_point = 0
    n_pos = df.shape[0]

    for i in range(0,n_pos,window_size):
        if i == 0:
            df_tmp = df.loc[i:i + window_size - 1,['window.pos']]
            df_list.append(df_tmp.rename(columns={'window.pos':'window_'+str(i)}).T)
            continue
        if i + window_size > n_pos:
            df_tmp = df.loc[i:n_pos-1,['window.pos']]
            df_tmp = df_tmp.rename(columns={'window.pos':'window_'+str(i)}).T
            last_columns = df_tmp.shape[1]
            df_tmp.columns = df_list[0].columns[0:last_columns]
            #df_list.append(df_tmp)
            break
        df_tmp = df.loc[i:i + window_size - 1,['window.pos']]
        df_tmp = df_tmp.rename(columns={'window.pos':'window_'+str(i)}).T
        df_tmp.columns = df_list[0].columns
        df_list.append(df_tmp)

    df_print = pd.concat(df_list)
    df_print.insert(0, column = 'descr',value=df_print.index)
    df_print.to_csv(target_file,sep='\t',header=False)
    file_append = open(target_file,'a')
    file_append.write(df_tmp.index[0]+'\t')
    file_append.write(df_tmp.index[0])
    for element in df_tmp.values[0]:
        file_append.write('\t' + str(element))
    file_append.close()

def window_build_w_overlap(source_file, target_file, window_size = 80):
    df_t = pd.read_csv(source_file,delimiter='\t')
    # extract overlaping windows
    df = pd.DataFrame(columns=['window.pos'])

    df['window.pos'] = df_t['window.chrom'] + '_' + df_t['window.pos'].map(str)
    df_list = list()
    start_point = 0
    n_pos = df.shape[0]

    for i in range(0,n_pos):
        if i == 0:
            df_tmp = df.loc[i:i + window_size - 1,['window.pos']]
            df_list.append(df_tmp.rename(columns={'window.pos':'window_'+str(i)}).T)
            continue
        if i + window_size > n_pos:
            df_tmp = df.loc[i:n_pos-1,['window.pos']]
            df_tmp = df_tmp.rename(columns={'window.pos':'window_'+str(i)}).T
            last_columns = df_tmp.shape[1]
            df_tmp.columns = df_list[0].columns[0:last_columns]
            #df_list.append(df_tmp)
            break
        df_tmp = df.loc[i:i + window_size - 1,['window.pos']]
        df_tmp = df_tmp.rename(columns={'window.pos':'window_'+str(i)}).T
        df_tmp.columns = df_list[0].columns
        df_list.append(df_tmp)
    
    df_print = pd.concat(df_list)
    df_print.insert(0, column = 'descr',value=df_print.index)
    df_print.to_csv(target_file,sep='\t',header=False)
    file_append = open(target_file,'a')
    file_append.write(df_tmp.index[0]+'\t')
    file_append.write(df_tmp.index[0])
    for element in df_tmp.values[0]:
        file_append.write('\t' + str(element))
    file_append.close()