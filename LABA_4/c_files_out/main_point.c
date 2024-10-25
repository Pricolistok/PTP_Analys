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

int main()
{
    int arr[N], *point_begin = arr, *point_end = point_begin + N;
    long long unsigned begin, end;
    input_arr(point_begin, point_end);
    // Сортировка массива
    begin = time_now();
    sort_mas(point_begin, point_end);
    end = time_now();
    *arr = *(arr + 1);
    *(arr + 1) = 1234;
    printf("%llu\n", end - begin);
    return 0;
}