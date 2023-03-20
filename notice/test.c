
#include <stdio.h>

typedef struct
{
    char name[20]; // name은 배열의 첫번째 원소를 가리키는 포인터입니다
    int mid;
    int fin;
} Student; // typedef를 사용하면 더 편하게 struct를 사용할 수 있습니다

int main()
{
    // Student myStudent;
    // Student *studentPointer; // 포인터가 가리키는 대상을 명시해 주지 않으면 오류가 발생합니다

    // scanf("%d", &(studentPointer->mid)); // studentPointer는 포인터이지만, mid는 int, 즉 포인터가 아니므로 &로 주소를 표시해주어야 합니다.
    // scanf("%d", &(studentPointer->fin));
    // scanf("%s", studentPointer->name); // name은 배열의 첫 원소의 주소를 가리키는 포인터이므로 &을 붙이면 안됩니다
    int *p;
    // scanf("%d", p);
    printf("%d\n", *p);
    // // printf("name : %s, mid : %d, fin : %d\n", myStudent.name, myStudent.mid, myStudent.fin);
    // printf("name : %s, mid : %d, fin : %d\n", studentPointer->name, studentPointer->mid, studentPointer->fin);
}
