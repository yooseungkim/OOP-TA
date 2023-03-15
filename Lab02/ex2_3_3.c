#include <stdio.h>
#include <string.h>

typedef struct student
{
    char name[20];
    int mat, eng;
} Student;

int main()
{
    int max = 0;
    char max_name[20];
    int n;

    printf("Enter the number of students : ");
    scanf("%d", &n);

    int i = 0;
    for (i = 0; i < n; i++)
    {
        int mat, eng;
        char name[20];
        scanf("%s %d %d", name, &mat, &eng);
        if (mat > max)
        {
            max = mat;
            strcpy(max_name, name);
        }
    }

    printf("highest math score : %s", max_name);
    return 0;
}
