#include <stdio.h>

#define i_len 2
#define j_len 3
#define k_len 4

int main(void)
{
    int arr[i_len][j_len][k_len], elem = 0;
    for (int i = 0; i < i_len; i++)
    {
        for (int j = 0; j < j_len; j++)
        {
            for (int k = 0; k < k_len; k++)
            {
                arr[i][j][k] = elem;
                elem++;
            }
        }
    }
    printf("%ld\n", sizeof(arr));
    return 0;
}