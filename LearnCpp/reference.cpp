#include<iostream>
using namespace std;
void swap(int& x, int& y);

int main()
{
    int i;
    double d;

    int& ii = i;
    double& dd = d;

    i = 5;
    cout << "Value of i : " << i << endl;
    cout << "Value of i reference : " << ii << endl;

    d = 11.7;
    cout << "Value of d : " << d << endl;
    cout << "Value of d reference : " << dd << endl;
//------------------------------------------------------------
    int a = 100;
    int b = 200;
    cout << "before a " << a << endl;
    cout << "before b " << b << endl;
    swap(a, b);
    cout << "after a " << a << endl;
    cout << "after b " << b << endl;

    return 0;
}

void swap(int& x, int& y)
{
    int temp;
    temp = x;
    x = y;
    y = temp;

    return;
}