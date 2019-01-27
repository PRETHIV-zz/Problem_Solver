//Add_Odd_E_Or_O
#include<iostream>
using namespace std;
int main()
{
int n;
cin>>n;
int s=0;
while(n>0){
    int t=n%10;
    if(t%2==1){
        s+=t;
    }
    n=n/10;
}
if(s%2==0){
cout<<"E";
}
else{
cout<<"O";
}
return 0;
}
