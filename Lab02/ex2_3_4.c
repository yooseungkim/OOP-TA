#include <stdio.h>

#define NAME_LEN 64

typedef struct
{
    char name[NAME_LEN];
    int height;
    float weight;
    long scholarship;
} Student;

void change(Student *std)
{
    std->height = std->height >= 180 ? std->height : 180;
    std->weight = std->weight >= 80 ? 80 : std->weight;
}

int main()
{
    Student gildong = {"Gildong", 173, 86.2};
    printf("name = %s %p\n", gildong.name, &gildong.name);
    printf("height = %d %p\n", gildong.height, &gildong.height);
    printf("weight = %f %p\n", gildong.weight, &gildong.weight);
    printf("scholarship = %ld %p\n", gildong.scholarship, &gildong.scholarship);

    change(&gildong);

    printf("name = %s %p\n", gildong.name, &gildong.name);
    printf("height = %d %p\n", gildong.height, &gildong.height);
    printf("weight = %f %p\n", gildong.weight, &gildong.weight);
    printf("scholarship = %ld %p\n", gildong.scholarship, &gildong.scholarship);

    return 0;
}