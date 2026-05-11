#include<iostream>
using namespace std;

class Student {
private:
    string name;
    int roll_no;
    int total_class;
    int attended_class;

public:
    Student(string n,int r) {
        name = n;
        roll_no = r;
        total_class = 0;
        attended_class = 0;
    }

    void mark_attendence(int total,int attended) {
        total_class = total;
        attended_class = attended;
    }

    float get_percentage() {
        if(total_class == 0) {
            cout << "No Classes Recorded Yet"<<endl;
            return 0;
        }

        float percentage = (attended_class * 100.0) / total_class;
        cout << "Attendance Percentage : " << percentage << "%" << endl;
        return percentage;
    }

    void display_records() {
        cout << "Name : " << name << endl;
        cout << "Roll No : " << roll_no << endl;
        cout << "Total Classes : " << total_class << endl;
        cout << "Attended Classes : " << attended_class << endl;
    }

    void defaulter_list() {
        float percentage = (attended_class * 100.0) / total_class;

        if(percentage < 75)
            cout << "Student is Defaulter" << endl;
        else
            cout << "Student is not Defaulter" << endl;
    }

    friend void search_student(Student s,int roll);
};


void search_student(Student s,int roll) {
    if(s.roll_no == roll)
       cout << "Roll Number Found" << endl;
    else
       cout << "Roll Number Not Found" << endl;
}


class sports_attendence : public Student {
    int total_sports_class , attended_sports_class;
public:
    sports_attendence(string n , int r, int total_sports , int attended_sports)
    : Student(n , r) {
        total_sports_class = total_sports;
        attended_sports_class = attended_sports;
    }
    
    float sports_percentage() {
        if(total_sports_class == 0) {
            cout << "No sports class recorded yet!" << endl;
            return 0;
        }
        float percentage = (attended_sports_class * 100.0) / total_sports_class;
        cout << "Sports Attendance Percentage = " << percentage << "%" << endl;
        return percentage;
    }

    void display_record() {
        Student::display_records();
        cout << "Total Sports Classes : " << total_sports_class << endl;
        cout << "Attended Sports Classes : " << attended_sports_class << endl;
    }
};

int main() {
    string n;
    int r;
    int roll; 

    cout << "Enter student name : ";
    cin >> n;

    cout << "Enter roll number : ";
    cin >> r;

    Student s1(n,r);

    int total_class, attended_class;

    cout << "Enter total classes : ";
    cin >> total_class;

    cout << "Enter attended classes : ";
    cin >> attended_class;

    s1.mark_attendence(total_class, attended_class);

    s1.display_records();
    s1.get_percentage();
    s1.defaulter_list();

    cout << "Enter roll no to search : ";
    cin >> roll;
    search_student(s1, roll);


    int total_sports, attended_sports;
    cout << "Enter total sports classes : ";
    cin >> total_sports;
    cout << "Enter attended sports classes : ";
    cin >> attended_sports;

    sports_attendence s2(n , r , total_sports , attended_sports);
    s2.mark_attendence(int total , int attended);
    s2.display_record();
    s2.sports_percentage();

    return 0;
}
