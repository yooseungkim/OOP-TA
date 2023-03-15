#include <stdio.h>
#include <stdlib.h>
typedef struct ans
{
    int count;
    int *array;
} Answer;

Answer find_all_in_array(int *arr, int key)
{
    int count = 0;
    int *ans = (int *)calloc(count + 1, sizeof(int));
    int i = 0;
    for (i = 0; i < 10; i++)
    {
        if (arr[i] == key)
        {
            ans[count] = i;
            count++;
            ans = (int *)realloc(ans, count + 1);
        }
    }

    Answer answer = {count, ans};
    return answer;
}

int main()
{
    printf("Enter 10 integers : ");
    int array[10];
    int key;
    int i = 0;
    for (i = 0; i < 10; i++)
    {
        scanf("%d", &array[i]); // do not put blank space after %d
    }
    for (i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");

    printf("Key value : ");
    scanf("%d", &key);

    Answer ans = find_all_in_array(array, key);
    if (ans.count)
    {
        printf("All found %d items\n", ans.count);
        printf("Index of found items : ");
        for (i = 0; i < ans.count; i++)
        {
            printf("%d ", ans.array[i]);
        }
        printf("\n");
    }
    else
    {
        printf("%d not found", key);
    }

    return 0;
}
