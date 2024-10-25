from math import sqrt
import sys

##  Подсчет rse
def main(path_file):
    flag = 0
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
        if t_avg != 0:
            rse = stdErr * 100 / t_avg 
            if rse >= 1:
                sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1])