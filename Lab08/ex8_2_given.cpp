#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>
using namespace std;

class Date 
{
private:
	char* day;
	int time[10];

public:
	Date(char* d, int* t, int size) 
	{
		int i;
		day = new char[strlen(d) + 1];
		strcpy(day, d);
		for (i = 0; i < size; i++)
			time[i] = t[i];
		time[i] = -1;
	}

	~Date() 
	{
		cout << "day" << endl;
		delete[] day;
	}

	void setDate(char* d) 
	{
		delete[] day;
		day = new char[strlen(d) + 1];
		strcpy(day, d);
	}

	int* getTime() 
	{
		return time;
	}

	void print() 
	{
		cout << "Day of the week : " << day << endl;
		cout << "Time : ";
		int i = 0;

		while (time[i] != -1) 
		{
			cout << time[i] << " , ";
			i++;
		}
		cout << "class" << endl;
	}
};

class Room 
{
private:
	char name[20];
	int num;

public:
	Room(char* n, int nm) 
	{
		strcpy(name, n);
		num = nm;
	}

	void setName(char* n) 
	{
		strcpy(name, n);
	}

	void setNum(int nm) 
	{
		num = nm;
	}

	void print() 
	{
		cout << "Building name : " << name << endl;
		cout << "Room number : " << num << endl;
	}
};

class Info 
{
private:
	int s_num;

public:
	Date d;
	Room r;
	Info(char* day, int* t, int size, char* n, int nm, int s) 
		:
		d(day, t, size), r(n, nm) 
	{
		s_num = s;
	}

	void setSNum(int s) 
	{
		s_num = s;
	}

	void print() 
	{
		d.print();
		r.print();
		cout << "Number of students : " << s_num << endl;
	}
};

class Subj 
{
private:
	int code;
	char name[20];
	Info* p;
	bool flag;

public:
	Subj() 
	{}

	Subj(int code, char* name) 
	{
		this->code = code;
		strcpy(this->name, name);
		p = NULL;
		flag = false;
	}

	~Subj() 
	{
		cout << "p" << endl;
		if (flag)
			delete p;
	}

	void setCode(int code) 
	{
		this->code = code;
	}

	int getCode() 
	{
		return code;
	}

	void setP() 
	{
		delete p;
		p = NULL;
	}

	Info* getP() 
	{
		return p;
	}

	void setInfo() 
	{
		char day[10], name[20];
		int t[10];
		int size, nm, s, i;
		cout << "Enter the day of the week";
		cin >> day;
		cout << "Please enter the unit of time. (Example: Enter 3 for 3 hours)";
		cin >> size;
		cout << "Please enter the lecture time. (Example: Enter 1 2 3 for classes 1-3)";
		for (i = 0; i < size; i++)
			cin >> t[i];
		cout << "Enter the building name.";
		cin >> name;
		cout << "Room number :";
		cin >> nm;
		cout << "Number of students:";
		cin >> s;
		p = new Info(day, t, size, name, nm, s);
		flag = true;
	}

	void setFlag(bool b) 
	{
		flag = b;
	}

	bool getFlag() 
	{
		return flag;
	}

	void setName(char* name) 
	{
		strcpy(this->name, name);
	}

	char* getName() 
	{
		return name;
	}

	void print() 
	{
		cout << " code:" << code << ", name : " << name << endl;
	}

	void printInfo() 
	{
		if (p != NULL) 
		{
			p->print();
		}
	}
};

class Staff 
{
private:
	Subj* sp[10];
	int num;

public:
	Staff() 
	{
		num = 0;
	}

	void input(int code, char* name) 
	{
		int i;
		bool f = true;
		for (i = 0; i < num; i++) {
			if (sp[i]->getCode() == code || !strcmp(sp[i]->getName(), name)) {
				f = false;
				cout << "This course is already registered." << endl;
			}
		}

		if (f)
			sp[num++] = new Subj(code, name);
	}

	~Staff() {
		int i;
		cout << "sp" << endl;
		for (i = 0; i < num; i++)
			delete sp[i];
	}

	void cancel(int code) {
		int i, j = -1;
		for (i = 0; i < num; i++) {
			if (sp[i]->getCode() == code) {
				j = i;
				break;
			}
		}

		if (j != -1) {
			for (i = j; i < num - 1; i++) {
				sp[i] = sp[i + 1];
			}
			num--;
		}
		else {
			cout << "There is no subject code to delete." << endl;
		}
	}

	void print() {
		int i;
		for (i = 0; i < num; i++)
			sp[i]->print();
	}

	Subj** getSp() {
		return sp;
	}

	int getNum() {
		return num;
	}
};

class Prof 
{
private:
	char name[10];
	char dept[20];
	Subj* s[5];
	int cnt;

public:
	Prof(char* n, char* d) {
		strcpy(name, n);
		strcpy(dept, d);
		cnt = 0;
	}

	void open(Staff* s1) {
		int x, i;
		bool f = false;
		Subj** ap = s1->getSp();
		s1->print();

		cout << "Enter the subject code to open";
		cin >> x;

		for (i = 0; i < s1->getNum(); i++) {
			if (x == ap[i]->getCode()) {
				if (!ap[i]->getFlag()) {
					ap[i]->setInfo();
					s[cnt] = ap[i];
					cnt++;
				}
				else {
					cout << "This course has already been opened." << endl;
				}
				f = true;
				break;
			}
		}

		if (!f)
			cout << "This is a subject code that does not exist." << endl;
	}

	void cancel() {
		int code, i, j = -1;
		cout << "Please enter the course code to cancel" << endl;
		cin >> code;

		for (i = 0; i < cnt; i++) {
			if (code == s[i]->getCode()) {
				j = i;
				s[i]->setFlag(false);
				s[i]->setP();
				break;
			}
		}

		if (j == -1)
			cout << "There are no related subjects." << endl;
		else {
			for (i = j; i < cnt - 1; i++)
				s[i] = s[i + 1];
			cnt--;
		}
	}

	void edit() {
		int i, j = -1, code, x, size, num, snum;
		char day[10], name[20];
		int* time = NULL;

		cout << "Enter the code of the subject to be modified" << endl;
		cin >> code;

		for (i = 0; i < cnt; i++) {		

			if (i == cnt)
				cout << "There are no related subjects." << endl;
			else {
				cout << "1. Modification of time 2. Modification of classroom 3. Modification of number of students" << endl;
				cin >> x;
				switch (x) {
				case 1:
					cout << "Day of the week:";
					cin >> day;
					cout << "unit of time";
					cin >> size;
					cout << "lecture time";
					time = s[i]->getP()->d.getTime();
					for (j = 0; j < size; j++)
						cin >> time[j];
					time[j] = -1;
					s[i]->getP()->d.setDate(day);					
					break;

				case 2:
					cout << "Building name: ";
					cin >> name;
					cout << "Room number: ";
					cin >> num;
					s[i]->getP()->r.setName(name);
					s[i]->getP()->r.setNum(num);
					break;

				case 3:
					cout << "Number of students:";
					cin >> snum;
					s[i]->getP()->setSNum(snum);
					break;

				default:
					cout << "You entered incorrectly." << endl;
				}
			}
		}
	}

	void print() {
		int i;
		cout << "professor name:" << name << endl;
		cout << "Department:" << dept << endl;
		for (i = 0; i < cnt; i++) {
			s[i]->print();
			if (s[i]->getFlag())
				s[i]->getP()->print();
		}
	}
};

class Stud 
{
private:
	char name[10];
	char dept[20];
	Subj* s[5];
	int cnt;

public:
	Stud(char* n, char* d) {
		strcpy(name, n);
		strcpy(dept, d);
		cnt = 0;
	}

	void select(Staff* s1) {
		int x, i;
		bool f = false;
		Subj** ap = s1->getSp();

		for (i = 0; i < s1->getNum(); i++) {
			if (ap[i]->getFlag()) {
				ap[i]->print();
				ap[i]->printInfo();
			}
		}

		cout << "Enter the subject code you wish to apply for";
		cin >> x;

		for (i = 0; i < cnt; i++) {
			if (x == s[i]->getCode()) {
				cout << "This subject has already been applied for." << endl;
				return;
			}
		}

		for (i = 0; i < s1->getNum(); i++) {
			if (x == ap[i]->getCode()) {
				s[cnt] = ap[i];
				cnt++;
				f = true;
				break;
			}
		}

		if (!f)
			cout << "This is a subject code that does not exist." << endl;
	}

	void cancel() {
		int code, i, j = -1;

		cout << "Please enter the course code to cancel" << endl;
		cin >> code;

		for (i = 0; i < cnt; i++) {
			if (code == s[i]->getCode()) {
				j = i;
				break;
			}
		}

		if (j == -1)
			cout << "There are no related subjects." << endl;
		else {
			for (i = j; i < cnt - 1; i++)
				s[i] = s[i + 1];
			cnt--;
		}
	}

	void print() {
		int i;
		cout << "Student name:" << name << endl;
		cout << "Department name:" << dept << endl;
		for (i = 0; i < cnt; i++) {
			s[i]->print();
		}
	}
};

int main() 
{
	Staff s1;
	Prof* f1;
	Stud* st;
	int x, code, y;
	char name[20], dept[20];
	bool flag1 = true, flag2 = true;
	while (flag1) {
		cout << "1.Faculty 2.Professor 3.Student" << endl;
		cin >> y;
		switch (y) {
		case 1:
			while (flag2) {
				cout << "1. Course registration 2. Course cancellation 3. Printing" << endl;
				cin >> x;
				switch (x) {
				case 1:
					cout << "Subject name:";
					cin >> name;
					cout << "Subject code:";
					cin >> code;
					s1.input(code, name);
					break;

				case 2:
					cout << "Subject code:" << endl;
					cin >> code;
					s1.cancel(code);
					break;

				case 3:
					s1.print();
					break;

				default:
					flag2 = false;
				}
			}

			break;

		case 2:
			flag2 = true;
			cout << "professor name:" << endl;
			cin >> name;
			cout << "Department name:" << endl;
			cin >> dept;
			f1 = new Prof(name, dept);
			while (flag2) {
				cout << "1. Course opening 2. Course opening cancellation 3. Open information correction 4. Open information output" << endl;
				cin >> x;

				switch (x) {
				case 1:
					f1->open(&s1);
					break;

				case 2:
					f1->cancel();
					break;

				case 3:
					f1->edit();
					break;

				case 4:
					f1->print();
					break;

				default:
					flag2 = false;
				}
			}

			break;

		case 3:
			flag2 = true;
			cout << "Student name:" << endl;
			cin >> name;
			cout << "Department name:" << endl;
			cin >> dept;
			st = new Stud(name, dept);
			while (flag2) {
				cout << "1. Course registration 2. Registration cancellation 3. Course information output" << endl;
				cin >> x;
				switch (x) {
				case 1:
					st->select(&s1);
					break;

				case 2:
					st->cancel();
					break;

				case 3:
					st->print();
					break;

				default:
					flag2 = false;
				}
			}

			break;

		default:
			cout << "entered incorrectly" << endl;
			flag1 = false;
		}
	}

	return 0;
}
