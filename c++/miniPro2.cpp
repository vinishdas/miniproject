#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string name;
    string USN;

    int marksMath,marksEng,marksPhy;
    float per;
    void input();
    void printLlist(int);
    void percentage(int,int,int);
    Student()
    {
        // printLlist(100);
    }
};


void Student::percentage(int phy,int math,int eng){
    per = float((phy+math+eng)/3);
}
void Student::printLlist(int num)
{   
    cout << num <<setw(10)<< name << setw(10) << USN<<setw(10)<< per<<"%" << endl;
}

void Student::input()
{
    cout << "---------input------------" << endl;
    cout << "Enter name:";
    cin >> name;
    cout << "Enter USN:";
    cin >> USN;
    cout << "enter marks for math:";
    cin >> marksMath;
    cout << "enter marks for physics:";
    cin >> marksPhy;
    cout << "enter marks for English:";
    cin >> marksEng;
    percentage(marksEng,marksPhy,marksMath);
}

int main()
{
    int reply, range,numOfStd=0,j;
    float key;
    string filterName,filterUSN,studentUSN;
    Student arr[100];
    while (true)
    {
        cout << "----options----" << endl;
        cout << "1.enter data" << endl;
        cout << "2.display data" << endl;
        cout << "3.edit data" << endl;
        cout << "4.exit" << endl;
        cin >> reply;
        if (reply == 1)
        {
            cout << "enter input data range:";
            cin >> range;
            for (int i = 0; i < range; i++)
            {
                arr[i+numOfStd].input();
            }
            numOfStd+=range;
        }
        else if(reply ==2){
            for(int i = 1;i<numOfStd;i++){
                key = arr[i].per;
                filterName = arr[i].name;
                filterUSN = arr[i].USN;
                j=i-1;
                while(j>=0&&arr[j].per<=key){
                    arr[j+1].name=arr[j].name;
                    arr[j+1].per=arr[j].per;
                    arr[j+1].USN=arr[j].USN;
                    j =j-1;

                }
                arr[j+1].per = key;
                arr[j+1].name = filterName;
                arr[j+1].USN = filterUSN;
            }
            cout<<"no."<<setw(10)<<"NAME"<<setw(10)<<"USN"<< setw(10)<<"%"<<endl;
             for (int i = 0; i <numOfStd ; i++)
            {   
                arr[i].printLlist(i);
            }
            cout<<"-------------list----------------"<<endl;
        }
        else if(reply == 3)
        {
            cout<<"Enter student USN to edit :";
            cin>>studentUSN;
            


        }
        else if(reply ==4){
            exit(0);
        }
        else{
            cout<<"invalid";
        }
    }

    return 0;
}