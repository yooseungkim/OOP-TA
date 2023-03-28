#include <iostream>
#define GET_MIN(x, y, z) ((x < y ? x : y) < z ? (x < y ? x : y) \
                                              : z)
using namespace std;

int main()
{
    int n1, n2, n3;
    cin >> n1 >> n2 >> n3;
    cout << GET_MIN(n1, n2, n3) << endl;
    return 0;
}