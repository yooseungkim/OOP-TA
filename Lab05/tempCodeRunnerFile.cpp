Point operator+(const Point &other)
    {
        Point temp(this->x + other.x, this->y + other.y);
        return temp;
    }