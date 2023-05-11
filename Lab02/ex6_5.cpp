#include <iostream>
#include <string>
using namespace std;

class Shape {
protected:
	int x=0;
	int y=0;
	string color;
public:
	Shape(int x, int y, const string& color)
	:x(x),y(y),color(color){
	}

	int getX() const {
		return x;
	}
	int getY() const {
		return y;
	}
	string getColor() const{
		return color;
	}

	virtual double getArea() const = 0;

};

class Circle :public Shape {
private:
	int r=0;
public:
	Circle(int x, int y, int r)
	: Shape(x, y,color), r(r) {}

	int getRadius() const {
			return r;
	}

	double getArea() const override {
		return 3.14 * r * r;
	}

};

int main() {
	Circle r{ 1, 1, 20 };
	cout << "Area of a circle: " << r.getArea() << endl;
	return 0;
}
