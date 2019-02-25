#include <iostream>
#include <cstring>
using namespace std;
const int MAX = 3;
// 函数声明
double getAverage(int *arr, int size);
void getSeconds(unsigned long *par);

int main()
{
    // 指针数组和数组指针
    /*
    定义 int (*p)[n];
()优先级高，首先说明p是一个指针，指向一个整型的一维数组，这个一维数组的长度是n，也可以说是p的步长。也就是说执行p+1时，p要跨过n个整型数据的长度。
如要将二维数组赋给一指针，应这样赋值：
int a[3][4];
int (*p)[4]; //该语句是定义一个数组指针，指向含4个元素的一维数组。
 p=a;        //将该二维数组的首地址赋给p，也就是a[0]或&a[0][0]
 p++;       //该语句执行过后，也就是p=p+1;p跨过行a[0][]指向了行a[1][]

所以数组指针也称指向一维数组的指针，亦称行指针。
    */
    int var[MAX] = {10,100,200};
    int *ptr[MAX];

    for(int i = 0;i < MAX;i ++)
    {
        ptr[i] = &var[i];
    }

    for(int i = 0;i < MAX;i ++)
    {
        cout << "Value of var[" << i << "] = ";
        cout<<*ptr[i]<<endl;
    }

    const char *names[MAX] = {
        "Zara Ali",
        "Hina Ali",
        "Nuha Ali",
    };

    for (int i = 0; i < MAX; i++)
    {
        cout << "Value of names[" << i << "] = ";
        cout << names[i] << endl;
    }
    
    // 传递指针给函数
    unsigned long sec;
    getSeconds(&sec);
    cout << "Number of seconds :" << sec << endl;

    // 接受数组作为函数的参数
    // 带有 5 个元素的整型数组
    int balance[5] = {1000, 2, 3, 17, 50};
    double avg;
    // 传递一个指向数组的指针作为参数
    avg = getAverage(balance, 5);
    // 输出返回值
    cout << "Average value is: " << avg << endl;

    return 0;

}

void getSeconds(unsigned long *par)
{
    // 获取当前的秒数
    *par = 888888;
    return;
}

double getAverage(int *arr, int size)
{
    int i, sum = 0;
    double avg;

    for (i = 0; i < size; ++i)
    {
        sum += arr[i];
    }

    avg = double(sum) / size;

    return avg;
}