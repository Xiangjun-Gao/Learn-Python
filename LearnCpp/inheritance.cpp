#include <iostream>

using namespace std;

class Shape
{
    public:
        void setWidth(int w)
        {
            width = w;
        }

        void setHeight(int h)
        {
            height = h;
        }
        Shape()
        {
            width = 10;
            height =10;
        }

    protected:
        int width;
        int height;
};

class Rectangle:public Shape
{
    public:
        int getArea()
        {
            return (width*height);
        }
};

void test1()
{
    Rectangle Rect;

    Rect.setWidth(5);
    Rect.setHeight(7);

    cout << "Total area: " << Rect.getArea() << endl;

    return;
}

/*
一个派生类继承了所有的基类方法，但下列情况除外：

基类的构造函数、析构函数和拷贝构造函数。
基类的重载运算符。
基类的友元函数。
*/

//-------------------------多继承-------------------

// 基类 PaintCost
class PaintCost
{
  public:
    int getCost(int area)
    {
        return area * 70;
    }
};

class Rectangle : public Shape, public PaintCost
{
  public:
    int getArea()
    {
        return (width * height);
    }
};

void test2(void)
{
    Rectangle Rect;
    int area;

    Rect.setWidth(5);
    Rect.setHeight(7);

    area = Rect.getArea();

    // 输出对象的面积
    cout << "Total area: " << Rect.getArea() << endl;

    // 输出总花费
    cout << "Total paint cost: $" << Rect.getCost(area) << endl;

    return ;
}