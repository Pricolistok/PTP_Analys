// Доколин Георгий ИУ7-22Б
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <time.h>


#ifndef N
#error Error input len
#endif

void sort_mas(int arr[], size_t len_arr);
void input_arr(int arr[], size_t len_arr);
unsigned long long time_now(void);
int cnt_time_work(int arr[], size_t len_arr);

unsigned long long time_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) - 1;
    
    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL;
    
}

// Сортировка массива вставками
void sort_mas(int arr[], size_t len_arr)
{
    int temp;
    size_t j;
    // Сортировка втсавками
    for (size_t i = 1; i < len_arr; i++)
    {
        temp = *(arr + i);
        j = i;
        while (j > 0 && *(arr + j - 1) > temp)
        {
            *(arr + j) = *(arr + j - 1);
            j -= 1;
        }
        *(arr + j) = temp;
    }
}

// Функция ввода массива
void input_arr(int arr[], size_t len_arr)
{
    for (int i = 0; i < (int)len_arr; i ++)
    {
        *(arr + i) = i % 231;
    }
}


int cnt_time_work(int arr[], size_t len_arr)
{
    long long unsigned begin, end;
    input_arr(arr, len_arr);
    begin = time_now();
    sort_mas(arr, len_arr);
    end = time_now();
    return end - begin;
}


int main()
{
    int arr[N];
    size_t len_arr = N;
    int cnt_iter = 0, time_work;
    double sum_time, rse = 2, t_avg = 4, diff_sum, s_2, s_1, stdErr;
    for (int i = 0; i < 24; i++)
    {
            cnt_iter++;
            time_work = cnt_time_work(arr, len_arr);
            sum_time += time_work;
            t_avg = sum_time / cnt_iter;
            diff_sum += (time_work - t_avg) * (time_work - t_avg);
            printf("%d \n", time_work);
    }
    while (rse >= 1.0)
    {
        cnt_iter++;
        time_work = cnt_time_work(arr, len_arr);
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