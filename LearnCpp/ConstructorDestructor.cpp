#include<iostream>
using namespace std;

class Line
{
    public:
        void setLength(double len);
        double getLength(void);
        Line(double l);
        ~Line();
    private:
        double length;
};

Line::Line(double l):length(l)
{
    cout << "Object is being created" << endl;
}

Line::~Line(void)
{
    cout << "Object is being deleted" << endl;
}

void Line::setLength(double len)
{
    length = len;
}

double Line::getLength(void)
{
    return length;
}
// 程序的主函数
int main()
{
    Line line(123);
    cout << "Length of line : " << line.getLength() << endl;
    // 设置长度
    line.setLength(6.0);
    cout << "Length of line : " << line.getLength() << endl;

    return 0;
}