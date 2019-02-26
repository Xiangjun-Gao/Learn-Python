#include <iostream>
using namespace std;

//-------------------------public-----------------------
class Line
{
  public:
    double length;
    void setLength(double len);
    double getLength(void);
};

double Line::getLength(void)
{
    return length;
}

void Line::setLength(double len)
{
    length = len;
    return;
}

void test1(void)
{
    Line line;

    line.setLength(6.0);
    cout << "Length of line:" << line.getLength() << endl;

    line.length = 10.0;
    cout << "Length of line:" << line.getLength() << endl;

    return;
}

//-------------------------private-----------------------
class Box
{
    public:
        double length;
        void setWidth(double wid);
        double getWidth(void);
    private:
        double width;
};

double Box::getWidth(void)
{
    return width;
}

void Box::setWidth(double wid)
{
    width = wid;
    return;
}

void test2()
{
    Box box;

    // 不使用成员函数设置长度
    box.length = 10.0; // OK: 因为 length 是公有的
    cout << "Length of box : " << box.length << endl;

    // 不使用成员函数设置宽度
    // box.width = 10.0; // Error: 因为 width 是私有的
    box.setWidth(10.0); // 使用成员函数设置宽度
    cout << "Width of box : " << box.getWidth() << endl;

    return;
}

//-------------------------protected-----------------------

class Box
{
  protected:
    double width;
};

class SmallBox : Box // SmallBox 是派生类
{
  public:
    void setSmallWidth(double wid);
    double getSmallWidth(void);
};

// 子类的成员函数
double SmallBox::getSmallWidth(void)
{
    return width;
}

void SmallBox::setSmallWidth(double wid)
{
    width = wid;
}

