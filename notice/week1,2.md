# QnA for Lab0 and Lab1

안녕하세요, 객체지향프로그래밍 조교 김유승입니다.

지난 두 주간 객체지향프로그래밍 수업에 많이 적응하셨길 바랍니다 :)

앞선 두 번의 실습에서 여러분들이 공통적으로 해주신 질문에 대해 답변을 해드리고, 추가적인 팁을 드리고자 합니다.

## Lab0

### 요약 코드

```c
#include <stdio.h>

typedef struct student { //student는 생략 가능
    char name[20]; // name은 배열의 첫번째 원소를 가리키는 포인터입니다
    int mid;
    int fin;
} Student; //typedef를 사용하면 더 편하게 struct를 사용할 수 있습니다

int main() {
    Student myStudent;
    Student *studentPointer = &myStudent; //초기화를 하지 않으면 오류가 발생할 수 있습니다

    scanf("%d", &(stduentPointer->mid)); // studentPointer는 포인터이지만, mid는 int, 즉 포인터가 아니므로 &로 주소를 표시해주어야 합니다.
    scanf("%d", &(studentPointer->fin));
    scanf("%s", studentPointer->name); //name은 배열의 첫 원소의 주소를 가리키는 포인터이므로 &을 붙이면 안됩니다

    printf("name : %s, mid : %d, fin : %d\n", myStudent.name, myStudent.mid, myStudent.fin);
}
```

### `typedef` 사용하기

`typedef`를 사용하여 `struct`를 더욱 편하게 사용할 수 있습니다.

`typedef`를 사용하게 된다면 구조체를 선언할 때 `struct student myStudent`가 아닌 `Student myStudnet`와 같이 간결하게 사용할 수 있습니다.
또한, `typedef`를 사용하는 경우, 가장 처음 `student`를 생략하고 마지막 `Student`만 있어도 좋습니다.

### 배열과 포인터의 관계 유의

`char name[20]`과 같이 배열을 나타내는 변수는 해당 배열의 **첫 번째 원소를 가리키는 포인터임을** 컴퓨터 프로그래밍 시간에 배우셨을 것입니다.
그러나 `scanf`와 같이 주소를 요구하는 몇몇 작업을 하다보면 이 사실을 잊는 경우가 있습니다.
특히, Lab0에서 `student` 구조체의 `name`을 `scanf`를 통해 입력받는 과정에서 오류를 범하는 학생이 많았습니다.
다른 `int`형 멤버 변수 를 처리하는 과정에서 혼돈이 생긴 것으로 예상되는데, 이에 유의하여 코딩을 하시면 좋을 것 같습니다.

### 구조체 포인터 이해

`student` 구조체의 포인터 사용에 관하여 헷갈려하는 학생이 간혹 있었습니다.
`struct student *p`라고 구조체 포인터 선언을 했다면, `p`는 포인터가 맞습니다.
따라서 멤버 변수에 접근할 때는 `p->mid`등과 같이 `->`(arrow pointer)를 통해 접근해야합니다.
그러나, `p`가 포인터라고 해서 `p->mid`가 포인터가 되는 것은 아닙니다.
왜냐하면 `mid`의 자료형은 `int*`가 아닌 `int`이기 때문입니다.
따라서, `scanf`로 해당 멤버 변수에 값을 주기 위해서는 `scanf("%d", &(p->mid))`와 같이 `&`로 주소를 나타내주어야 합니다.

### 포인터 변수의 초기화

마지막으로, 포인터 변수를 선언할 때 초기화를 해주지 않는 경우가 있었습니다.
이렇게 초기화되지 않은 포인터를 wild pointer이라고 하는데, 이 상태에서 해당 포인터의 값을 참조하면 문제가 발생합니다. (더 자세한 내용은 [여기](https://ko.wikipedia.org/wiki/%ed%97%88%ec%83%81_%ed%8f%ac%ec%9d%b8%ed%84%b0)에서 확인하시면 좋을 것 같습니다)
처음 선언과 동시에 초기화를 해주는 것이 좋으나, 이후에 초기화를 해주어도 됩니다.
Lab0의 경우, `struct Student *p`와 같이 포인터만 선언하고, 이 포인터가 가리킬 변수로 초기화시켜주지 않아 오류가 발생하는 경우가 있었습니다. (이 경우 `bus error`, `segmentation fault`와 같은 오류가 발생합니다)
따라서 포인터를 선언할 때는 되도록 초기화를 동시에 해주는 것이 바랍직합니다.

### Visual Studio의 빌드에서 제외

Visual Studio에서 하나의 솔루션에 여러 소스파일을 만들 수 있습니다. 여러분들이 실습시간에 연습문제를 다섯 개를 푼다면 보통 하나의 솔루션에 소스파일 다섯 개를 만들게 될 것입니다.
그런데, 각 소스파일에 `main()`이 정의되어있다면, 실행했을 때 `error LNK2005: main already defined in Source.obj`와 같은 에러를 출력할 것입니다. 이는 컴파일을 할 떄 `main()`은 하나여야하지만 각 소스파일에 여러 번 정의되어 나타나는 에러입니다.

이러한 문제는 다음과 같이 각 소스파일을 빌드에서 제외함으로써 해결할 수 있습니다.

우측 솔루션 탐색기 > 소스파일 우클릭 > 속성(properties) > 빌드에서 제외(Excluded from build) 우측 화살표 클릭 > 예로 변경
![image](./visual_studio_exclude_from_build.png)

이 방법으로 필요한 소스파일의 `main()`만 남기고 빌드에서 제외하면 정상적으로 실행됩니다.

## Lab1

### Multiplicity에 대하여

![uml](./uml.png)

ex1_2에서 화살표에 적힌 숫자가 무엇을 의미하는지 궁금해하는 학생이 많았습니다. 해당 숫자는 multiplicity, 즉 개수를 의미합니다.
예를 들어 위의 그림에서 `Customer`에는 `1`, `Orders`에는 `0..*`으로 되어있는데, 이를 통해 하나의 `Customer`는 여러 개(0개 포함)의 `Orders`를 가짐을 알 수 있습니다. 비슷하게, 하나의 `Orders`는 하나의 `Order Details`를 가짐을 알 수 있습니다.

multiplicity는 화살표를 클릭한 후 우측 하단의 properties 중 end1 multiplicity, end2 multiplicity 를 설정해줌으로써 UML에서 입력 가능합니다.

---

이상 많이 하신 질문에 대해 답변해드렸습니다.
이와 별개로, 추가적인 질문이 있으시다면 편하게 <yooseungkim@gm.gist.ac.kr> 이나 다른 TA에게 질문주시길 바랍니다 :)

모두 좋은 하루 보내세요 👍
