#include <iostream>
#include <string>

using namespace std;

class Book
{
    string title;
    string author;

public:
    Book(string title, string author) : title(title), author(author){};
    string getTitle() { return title; }
    string getAuthor() { return author; }
};

int main()
{
    Book b("C how to program with an introduction to C++", "Paul Deitel");
    cout << "Title: " << b.getTitle() << endl;
    cout << "Author: " << b.getAuthor() << endl;

    return 0;
}