#include <stdio.h>

typedef struct
{
    int number;
    char name[100];
    char phone[20];
    int age;
} Employee;

int main()
{
    Employee array[4] = {
        {1, "Gildong1", "1010", 10},
        {2, "Gildong2", "1010", 20},
        {3, "Gildong3", "1010", 25},
        {4, "Gildong4", "1010", 30},
    };

    int i = 0;
    for (i = 0; i < 4; i++)
    {
        if (20 <= array[i].age && 30 >= array[i].age)
        {
            printf("%s\n", array[i].name);
        }
    }

    return 0;
}