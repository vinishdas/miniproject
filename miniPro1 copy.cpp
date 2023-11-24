#include<bits/stdc++.h>
using namespace std;

int ranGen(int rag){
    return rand()%rag;
} 
void checknum(int number,int answer){
    if(number == answer)
    cout<<answer<<" is the right number";
    else if(answer-number>0)
    cout<<"too high";
}
int main()
{ srand(static_cast<unsigned int>(time(0)));
int number  = 1+rand()%100;

return 0;

}