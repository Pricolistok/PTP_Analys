// Доколин Георгий ИУ7-22Б
// Подключение библиотек
#include <stdio.h>
#include <math.h>

// Инициализация функции для проверки, является ли число простым
int is_simple(int num)
{
    // Цикл для проверки делителей
    for (int i = num - 1; i > 1; i--)
    {
        if (num % i == 0)
        {
            return 1;
        }
    }
    return 0;
}
// Инициализация функции
int main()
{
    // Инициализация переменных
    int a, dividor, rc, saver;
    // Ввод значений
    rc = scanf("%d", &a);
    // Делитель
    saver = a;
    dividor = 2;
    // Проверка корректности данных
    if (rc != 1 || a < 1)
    {
        printf("Error \n");
        return 1;
    }
    // Обработка условия и завершение программы, если а = 1
    if (a == 1)
    {
        return 0;
    }
    // Проверка на простоту чила а
    if (is_simple(a) == 0)
    {
        printf("%d", a);
    }
    else
    {
    // Цикл для деления числа, пока оно не станет равно 1
        while ((a > 1 || a % dividor == 0) && dividor < saver)
        {
            if (is_simple(dividor) == 0 && a % dividor == 0)
            {
                a = a / dividor;
                printf("%d ", dividor);
            }
            else
            {
                dividor = dividor + 1;
            }
        }
    }
    return 0;
}