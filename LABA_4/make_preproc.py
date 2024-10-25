from math import sqrt

## Подсчет RSE
def rse_cnt(path_file):
    with open(path_file, 'r') as file:
        sum_t = 0
        cnt = 0
        sum_diff = 0
        for i in file:
            sum_t += int(i)
            cnt += 1
        t_avg = sum_t / cnt
        file.seek(0)
        for i in file:
            sum_diff += (int(i) - t_avg) ** 2
        s_2 = (1 / (cnt - 1)) * sum_diff
        s_1 = sqrt(s_2)
        stdErr = s_1 / sqrt(cnt)
        if t_avg == 0:
            return 0
        rse = stdErr * 100 / t_avg 
        return rse
    
## Запись информации в файл
def write_info(directory, directory_opt, file_data, file_preproc, num):
    arr_data = list(map(int, list(file_data)))
    arr_data.sort()
    len_data = len(arr_data)
    summ_data = sum(arr_data)
    file_preproc.write(str(summ_data / len_data) + '\n')
    if len_data % 2 == 0:
        median = (arr_data[len_data // 2] + arr_data[(len_data // 2) - 1]) / 2
    else:
        median = arr_data[len_data // 2]
    file_preproc.write(str(median) + '\n')
    file_preproc.write(str(min(arr_data)) + '\n')
    file_preproc.write(str(max(arr_data)) + '\n')
    file_preproc.write(str(arr_data[len_data // 4]) + '\n')
    file_preproc.write(str(arr_data[len_data // 2]) + '\n')
    file_preproc.write(str(arr_data[3 * len_data // 4]) + '\n')
    rse = rse_cnt(f'./data{directory}/data{directory_opt}/{num}.txt')
    file_preproc.write(str(rse) + '\n')
    file_preproc.write(str(len_data) + '\n')
    

def main():
    # Сбор данных по каждому файлу
    with open('settings.txt', 'r') as settings_file:
        arr_settings = settings_file.readline().split()
        start = int(arr_settings[1])
        finish = int(arr_settings[3])
        step = int(arr_settings[5])
    for directory in ['_in', '_out']:
        for directory_opt in ['_formal', '_index', '_point']:
            for num in range(start, finish + 1, step):
                with open(f'./data{directory}/data{directory_opt}/{num}.txt', 'r') as file_data:
                    with open(f'./preproc_data{directory}/data{directory_opt}/{num}.txt', 'a+') as file_preproc:
                        write_info(directory, directory_opt, file_data, file_preproc, num)
    for directory_opt in ['_formal_tsc', '_index_tsc', '_point_tsc']:
        for num in range(start, finish + 1, step):
            with open(f'./data_in/data{directory_opt}/{num}.txt', 'r') as file_data:
                with open(f'./preproc_data_in/data{directory_opt}/{num}.txt', 'a+') as file_preproc:
                    write_info('_in', directory_opt, file_data, file_preproc, num)


if __name__ == '__main__':
    main()