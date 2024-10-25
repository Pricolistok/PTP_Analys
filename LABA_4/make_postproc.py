import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из файла
def read_settings():
    with open('settings.txt', 'r') as settings_file:
        arr_settings = settings_file.readline().split()
        start = int(arr_settings[1])
        finish = int(arr_settings[3])
        step = int(arr_settings[5])
    return [start, finish, step]

# Построение линейного графика с тиками
def create_line_graph_tsc(start, finish, step, label):
        # Подписываем оси
        plt.figure(figsize=(12,10))
        plt.title(f'Кусочно-линейный график зависимости времени выполнения от числа \n элементов массива. {label}', fontsize=17)
        plt.xlabel("Количество элементов массива")
        plt.ylabel("Время выполнения")
        plt.grid(True)
        # Построение графика
        x_formal = np.arange(start, finish + 1, step)
        y_formal = []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data_in/data_formal_tsc/{num}.txt', 'r') as file_data:
                arr_formal = file_data.readlines()
                y_formal.append(float(arr_formal[0]))
        y_formal = np.asarray(y_formal)

        plt.plot(x_formal, y_formal, marker='+',linestyle='solid')

        x_index = np.arange(start, finish + 1, step)
        y_index = []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data_in/data_index_tsc/{num}.txt', 'r') as file_data:
                arr_formal = file_data.readlines()
                y_index.append(float(arr_formal[0]))
        y_index = np.asarray(y_index)

        plt.plot(x_index, y_index, marker='+',linestyle='solid')
        

        x_point = np.arange(start, finish + 1, step)
        y_point = []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data_in/data_point_tsc/{num}.txt', 'r') as file_data:
                arr_point = file_data.readlines()
                y_point.append(float(arr_point[0]))
        y_point = np.asarray(y_point)
        plt.plot(x_point, y_point, marker='+',linestyle='solid')
        plt.legend(('Formal', 'Index', 'Point'))
        plt.savefig(f'postproc_data/line_in_tsc.svg')


# Построение графика с усами
def create_mustache_graph(type_set, start, finish, step, label):
        # Подпись осей
        plt.figure(figsize=(12,10))
        plt.title(f'График с усами. {label}', fontsize=17)
        plt.xlabel("Количество элементов массива")
        plt.ylabel("Время выполнения")
        plt.grid(True)
        # Построение графика
        x_index = np.arange(start, finish + 1, step)
        y_index = []
        kv_1_4 = []
        kv_3_4 = []
        mini_index, maxi_index = [], []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data{type_set}/data_index/{num}.txt', 'r') as file_data:
                arr_formal = file_data.readlines()
                y_index.append(float(arr_formal[0]))
                mini_index.append(float(arr_formal[0]) - float(arr_formal[2]))
                maxi_index.append(float(arr_formal[3]) - float(arr_formal[0]))
                kv_1_4.append(float(arr_formal[4]))
                kv_3_4.append(float(arr_formal[6]))
        kv_1_4 = np.asarray(kv_1_4)
        kv_3_4 = np.asarray(kv_3_4)
        y_index = np.asarray(y_index)
        error_formal = np.array([np.asarray(mini_index), np.asarray(maxi_index)])

        plt.errorbar(x_index, y_index, yerr=error_formal, marker='+',linestyle='solid',
            ecolor='red', elinewidth=0.8, capsize=4, capthick=1)
        plt.legend(['Index'])
        plt.plot([x_index, x_index], [kv_1_4, kv_3_4], label='Данные', color='green', linewidth=3)
        plt.savefig(f'postproc_data/mustache{type_set}.svg')


# Построение линейного графика
def create_line_graph(type_set, start, finish, step, label):
        # Подписываем оси
        plt.figure(figsize=(12,10))
        plt.title(f'Кусочно-линейный график зависимости времени выполнения от числа \n элементов массива. {label}', fontsize=17)
        plt.xlabel("Количество элементов массива")
        plt.ylabel("Время выполнения")
        plt.grid(True)
        # Построение по значениям
        x_formal = np.arange(start, finish + 1, step)
        y_formal = []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data{type_set}/data_formal/{num}.txt', 'r') as file_data:
                arr_formal = file_data.readlines()
                y_formal.append(float(arr_formal[0]))
        y_formal = np.asarray(y_formal)

        plt.plot(x_formal, y_formal, marker='+',linestyle='solid')

        x_index = np.arange(start, finish + 1, step)
        y_index = []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data{type_set}/data_index/{num}.txt', 'r') as file_data:
                arr_formal = file_data.readlines()
                y_index.append(float(arr_formal[0]))
        y_index = np.asarray(y_index)

        plt.plot(x_index, y_index, marker='+',linestyle='solid')
        

        x_point = np.arange(start, finish + 1, step)
        y_point = []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data{type_set}/data_point/{num}.txt', 'r') as file_data:
                arr_point = file_data.readlines()
                y_point.append(float(arr_point[0]))
        y_point = np.asarray(y_point)

        plt.plot(x_point, y_point, marker='+',linestyle='solid')
        plt.legend(('Formal', 'Index', 'Point'))
        plt.savefig(f'postproc_data/line{type_set}.svg')


# Построение графика с ошибкой
def create_error_graph(type_set, start, finish, step, label):
        # Подписываем оси
        plt.figure(figsize=(12,10))
        plt.title(f'Кусочно-линейный график с ошибкой. \n {label}', fontsize=17)
        plt.xlabel("Количество элементов массива")
        plt.ylabel("Время выполнения")
        plt.grid(True)
        # Построение 
        x_formal = np.arange(start, finish + 1, step)
        y_formal = []
        mini_formal, maxi_formal = [], []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data{type_set}/data_formal/{num}.txt', 'r') as file_data:
                arr_formal = file_data.readlines()
                y_formal.append(float(arr_formal[0]))
                mini_formal.append(float(arr_formal[0]) - float(arr_formal[2]))
                maxi_formal.append(float(arr_formal[3]) - float(arr_formal[0]))
        y_formal = np.asarray(y_formal)
        error_formal = np.array([np.asarray(mini_formal), np.asarray(maxi_formal)])

        plt.errorbar(x_formal, y_formal, yerr=error_formal, marker='+',linestyle='solid',
    ecolor='blue', elinewidth=0.8, capsize=4, capthick=1)

        x_index = np.arange(start, finish + 1, step)
        y_index = []
        mini_index, maxi_index = [], []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data{type_set}/data_index/{num}.txt', 'r') as file_data:
                arr_formal = file_data.readlines()
                y_index.append(float(arr_formal[0]))
                mini_index.append(float(arr_formal[0]) - float(arr_formal[2]))
                maxi_index.append(float(arr_formal[3]) - float(arr_formal[0]))
        y_index = np.asarray(y_index)
        error_index = np.array([np.asarray(mini_index), np.asarray(maxi_index)])

        plt.errorbar(x_index, y_index, yerr=error_index, marker='+',linestyle='solid',
    ecolor='orange', elinewidth=0.8, capsize=4, capthick=1)
        

        x_point = np.arange(start, finish + 1, step)
        y_point = []
        mini_point, maxi_point = [], []
        for num in range(start, finish + 1, step):
            with open(f'./preproc_data{type_set}/data_point/{num}.txt', 'r') as file_data:
                arr_point = file_data.readlines()
                y_point.append(float(arr_point[0]))
                mini_point.append(float(arr_point[0]) - float(arr_point[2]))
                maxi_point.append(float(arr_point[3]) - float(arr_point[0]))
        y_point = np.asarray(y_point)
        error_point = np.array([np.asarray(mini_point), np.asarray(maxi_point)])

        plt.errorbar(x_point, y_point, yerr=error_point, marker='+',linestyle='solid',
    ecolor='green', elinewidth=0.8, capsize=4, capthick=1)

        plt.legend(('Formal', 'Index', 'Point'))
        plt.savefig(f'postproc_data/error{type_set}.svg')


def main():
    start, finish, step = read_settings()
    ## Построение линейных графиков
    create_error_graph('_in', start, finish, step, 'Внутренний замер в милисекундах.')
    create_error_graph('_out', start, finish, step, 'Внешний замер в милисекундах.')

    create_line_graph_tsc(start, finish, step, 'Внутренний замер в тиках.')

    ## Построение графиков с ошибкой
    create_line_graph('_in', start, finish, step, 'Внутренний замер в милисекундах.')
    create_line_graph('_out', start, finish, step, 'Внешний замер в милисекундах.')

    
    ## Построение графиков с усами
    create_mustache_graph('_in', start, finish, step, 'Внутренний замер в милисекундах.')
    create_mustache_graph('_out', start, finish, step, 'Внешний замер в милисекундах.')



if __name__ == '__main__':
    main()