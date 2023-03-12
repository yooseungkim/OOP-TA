
#include <stdio.h>
#include <stdlib.h> //to use calloc / malloc
void spc(int *a, int *a_spc)
{
    int i = 0;
    int count = 0;
    for (i = 0; i < 7; i++)
    {
        a_spc[i] = a[i];
        if (a[i] == 1)
            count += 1;
    }
    if (count % 2 == 0)
        a_spc[7] = 0;
    else
        a_spc[7] = 1;
}

int main()
{
    int N = 7;
    int *a, *a_spc;
    a = (int *)calloc(N, sizeof(int));
    a_spc = (int *)calloc(N + 1, sizeof(int));
    printf("Enter a message vector of length %d : ", N);

    int i;
    for (i = 0; i < N; i++)
    {
        scanf("%d", &a[i]);
    }
    spc(a, a_spc);
    printf("The transmitted vecotr of length %d : ", N + 1);
    for (i = 0; i < N + 1; i++)
        printf("%d ", a_spc[i]);
    printf("\n");
}