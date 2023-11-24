#include<bits/stdc++.h>
using namespace std;

class area{
    private:
    int l,b,r;
    public:
    area(){
        l=2;
        b =3;
        r=5;

    }
void display(){
    cout<<l<<": lenght"<<endl;
    cout<<b<<": lenght"<<endl;
    cout<<r<<": lenght"<<endl;
}
   void areaspace(int lenght,int breath)
   {
    cout<<"area of rectangle : "<<lenght*breath<<endl;
   }
   void  areaspace(int);

};

void area::areaspace(int radius){
cout<<"area of cirlce "<<radius*radius*3.14;
}


int main()
{
    area a,b;
    a.display();
    a.areaspace(2,5);
    a.areaspace(5);
}