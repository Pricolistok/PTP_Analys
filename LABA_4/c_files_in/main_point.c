// Доколин Георгий ИУ7-22Б
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <time.h>

#ifndef N
#error Error input len
#endif

void sort_mas(int *point_begin, int *point_end);
void input_arr(int *point_begin, int *point_end);
unsigned long long time_now(void);
int cnt_time_work(int *point_begin, int *point_end);

unsigned long long time_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) - 1;
    
    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL;
    
}

// Сортировка массива вставками
void sort_mas(int *point_begin, int *point_end)
{
    int temp;
    int  *point_j;
    // Сортировка втсавками
    for (int *point_i = point_begin; point_i < point_end; point_i++)
    {
        temp = *point_i;
        point_j = point_i;
        while (point_j > point_begin && *(point_j - 1) > temp)
        {
            *point_j = *(point_j - 1);
            point_j--;
        }
        *point_j = temp;
    }
}

// Функция ввода массива
void input_arr(int *point_begin, int *point_end)
{
    int elem = 0;
    for (int *point_i = point_begin; point_i < point_end; point_i++)
    {
        *point_i = elem % 231;
        elem++;
    }
}


int cnt_time_work(int *point_begin, int *point_end)
{
    long long unsigned begin, end;
    input_arr(point_begin, point_end);
    begin = time_now();
    sort_mas(point_begin, point_end);
    end = time_now();
    return end - begin;
}


int main()
{
    int arr[N], *point_begin = arr, *point_end = point_begin + N;
    int cnt_iter = 0, time_work;
    double sum_time, rse = 2, t_avg = 4, diff_sum, s_2, s_1, stdErr;
    for (int i = 0; i < 24; i++)
    {
            cnt_iter++;
            time_work = cnt_time_work(point_begin, point_end);
            sum_time += time_work;
            t_avg = sum_time / cnt_iter;
            diff_sum += (time_work - t_avg) * (time_work - t_avg);
            printf("%d \n", time_work);
    }
    while (rse >= 1.0)
    {
        cnt_iter++;
        time_work = cnt_time_work(point_begin, point_end);
        sum_time += time_work;
        t_avg = sum_time / cnt_iter;
        diff_sum += (time_work - t_avg) * (time_work - t_avg);
        if (sum_time > 1)
        {
            s_2 = diff_sum / (cnt_iter - 1);
            s_1 = sqrt(s_2);
            stdErr = s_1 / sqrt(cnt_iter);
            rse = stdErr * 100 / t_avg;
            printf("%d \n", time_work);
        }
        else
        {
            printf("0\n");
            break;
        }
    }
    *arr = *(arr + 1);
    *(arr + 1) = 1234;
    return 0;
}