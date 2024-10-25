#include <stdio.h>

union data
{
    long long int lldnum_1;
    unsigned int ullnum_1;
    double double_num_1;
    int num_1; 
    char ch_1;   
};

int main(void)
{
    union data data_1;
    data_1.num_1 = 58683;
    data_1.double_num_1 = 4.67;
    printf("%lu \n", sizeof(data_1));
    printf("OK");    
    return 0;
}
