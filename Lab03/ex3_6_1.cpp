#include <iostream>

using namespace std;

class Date
{
    int m_month;
    int m_day;
    int m_year;

public:
    void setDate(int month, int day, int year);
    void setDay(int day);
    int getDay();
};

int main()
{
    Date today;
    today.setDate(3, 28, 2023);
    today.setDay(29);
    cout << today.getDay() << endl;
    return 0;
}

void Date::setDate(int month, int day, int year)
{
    m_month = month;
    m_day = day;
    m_year = year;
}

void Date::setDay(int day)
{
    m_day = day;
}

int Date::getDay()
{
    return m_day;
}