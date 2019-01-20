//occurence of k in n
#include<iostream>
using namespace std;
int main(){
int n,k;
cin>>n>>k;
int c=0;
while(n>0){
    if(k==(n%10)){
        c++;
    }
    n/=10;
}
cout<<c;
return 0;
}
