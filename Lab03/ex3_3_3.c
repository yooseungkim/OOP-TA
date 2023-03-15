#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    printf("how many elements? : ");
    scanf("%d", &n);
    int *array = (int *)calloc(n, sizeof(int));

    int i = 0;
    for (i = 0; i < n; i++)
    {
        printf("Enter element (integer) : ");
        scanf("%d", &array[i]);
    }
    printf("The entered values are\n");
    for (i = 0; i < n; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}