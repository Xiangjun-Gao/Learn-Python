#include <iostream>
using namespace std;
/*
数据抽象是指，只向外界提供关键信息，并隐藏其后台的实现细节，即只表现必要的信息而不呈现细节。
数据抽象是一种依赖于接口和实现分离的编程（设计）技术。

数据封装是一种把数据和操作数据的函数捆绑在一起的机制，
数据抽象是一种仅向用户暴露接口而把具体的实现细节隐藏起来的机制。
*/

/*
C++ 接口是使用抽象类来实现的，抽象类与数据抽象互不混淆:
    数据抽象是一个把实现细节与相关的数据分离开的概念。

如果类中至少有一个函数被声明为纯虚函数，则这个类就是抽象类。
纯虚函数是通过在声明中使用 "= 0" 来指定的
抽象类不能被用于实例化对象，它只能作为接口使用。如果试图实例化一个抽象类的对象，会导致编译错误。
*/
// 基类
class Shape
{
  public:
    // 提供接口框架的纯虚函数
    virtual int getArea() = 0;
    void setWidth(int w)
    {
        width = w;
    }
    void setHeight(int h)
    {
        height = h;
    }

  protected:
    int width;
    int height;
};

// 派生类
class Rectangle : public Shape
{
  public:
    int getArea()
    {
        return (width * height);
    }
};
class Triangle : public Shape
{
  public:
    int getArea()
    {
        return (width * height) / 2;
    }
};

int main(void)
{
    Rectangle Rect;
    Triangle Tri;

    Rect.setWidth(5);
    Rect.setHeight(7);
    // 输出对象的面积
    cout << "Total Rectangle area: " << Rect.getArea() << endl;

    Tri.setWidth(5);
    Tri.setHeight(7);
    // 输出对象的面积
    cout << "Total Triangle area: " << Tri.getArea() << endl;

    return 0;
}