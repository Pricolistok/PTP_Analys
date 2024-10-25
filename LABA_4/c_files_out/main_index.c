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
        temp = arr[i];
        j = i;
        while (j > 0 && arr[j - 1] > temp)
        {
            arr[j] = arr[j - 1];
            j -= 1;
        }
        arr[j] = temp;
    }
}

// Функция ввода массива
void input_arr(int arr[], size_t len_arr)
{
    for (int i = 0; i < (int)len_arr; i ++)
    {
        arr[i] = i % 231;
    }
}

int main()
{
    int arr[N];
    size_t len_arr = N;
    long long unsigned begin, end;
    input_arr(arr, len_arr);
    begin = time_now();
    sort_mas(arr, len_arr);
    end = time_now();
    arr[0] = arr[1];
    arr[1] = 1234;
    printf("%llu\n", end - begin);
    return 0;
}