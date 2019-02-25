#include <iostream>
#include<cstring>
using namespace std;

char greeting[6] = {'H','e','l','l','\0'};
//char greeting[] = "Hello"

int main()
{
    /*
    char str1[11] = "Hello";
    char str2[11] = "World";
    char str3[11];
    int len;

    strcpy(str3, str1);
    cout<<str3<<endl;

    strcat(str1, str2);
    cout<<str1<<endl;

    len = strlen(str1);
    cout<<len<<endl;
    */

    // string 
    string str1 = "Hello";
    string str2 = "World";
    string str3;
    int len;
    
    str3 = str1;
    cout<<str3<<endl;

    str3 = str1 + str2;
    cout<<str3<<endl;
    cout<<str3.size()<<endl;

    string

    return 0;
}
