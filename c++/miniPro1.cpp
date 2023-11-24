#include<bits/stdc++.h>
using namespace std;


void checknum(int number,int answer){
    if(number == answer)
    {cout<<answer<<" is the right number";
    exit(0);
    }
    else if(number>answer)
    cout<<"too high"<<endl;
    else
    cout<<"too low"<<endl;
}


int main()
{
srand(static_cast<unsigned int>(time(0))); 
int lb,ub,number,gussedNum,life=5;
cout<<"welcome to the number guessing game";
cout<<"what will be the range of number: "<<endl;
cin>>lb>>ub;
number = (rand()%(ub-lb+1))+lb;

cout<<"guess the number i am thinking: "<<endl;

while(true)
{ 
 cin>>gussedNum;
 checknum(gussedNum,number);
--life;
cout<<"you have "<<life<<"lives"<<endl;
if(life==0){
cout<<"game over you lost";
break;}
}
return 0;

}