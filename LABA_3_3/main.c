#include <stdio.h>

int main(void)
{
    char arr_1[][9] = {"January", "February", "March"};
    char *arr_2[] = {"January", "February", "March"};
    printf("%s %s", arr_1[0], arr_2[0]);
    return 0;
}

// #include <stdio.h>

// int main(void)
// {
//     char str[] ="Hello world!";
//     printf("%s\n", str);
//     return 0;
// }