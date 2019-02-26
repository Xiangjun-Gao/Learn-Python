#include <iostream>

using namespace std;

class Box
{
    public:
        double length;
        double breadth;
        double height;
        // 成员函数声明
        double getVolume(void);
        void setLength(double len);
        void setBreadth(double bre);
        void setHeight(double hei);
};

double Box::getVolume(void)
{
    return length*breadth*height;
}

void Box::setLength(double len)
{
    length = len;
}

void Box::setBreadth(double bre)
{
    breadth = bre;
}

void Box::setHeight(double hei)
{
    height = hei;
}

void test1(void)
{
    Box Box1;
    Box Box2;
    double volume = 0.0;

    Box1.height = 5.0;
    Box1.length = 6.0;
    Box1.breadth = 7.0;

    Box2.height = 10.0;
    Box2.length = 12.0;
    Box2.breadth = 13.0;

    volume = Box1.height * Box1.length * Box1.breadth;
    cout << "Box1 volume:" << volume << endl;
    volume = Box2.height * Box2.length * Box2.breadth;
    cout << "Box2 volume:" << volume << endl;

    return;
}

void test2(void)
{
    Box Box1;            // 声明 Box1，类型为 Box
    Box Box2;            // 声明 Box2，类型为 Box
    double volume = 0.0; // 用于存储体积

    // box 1 详述
    Box1.setLength(6.0);
    Box1.setBreadth(7.0);
    Box1.setHeight(5.0);

    // box 2 详述
    Box2.setLength(12.0);
    Box2.setBreadth(13.0);
    Box2.setHeight(10.0);

    // box 1 的体积
    volume = Box1.getVolume();
    cout << "Box1 V:" << volume << endl;

    // box 2 的体积
    volume = Box2.getVolume();
    cout << "Box2 V:" << volume << endl;
    return;
}

int main()
{
    test1();
    test2();
    return 0;
}