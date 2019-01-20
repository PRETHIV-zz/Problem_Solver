//hlo stalkers
#include<iostream>
using namespace std;
int main(){
int n,k;
cin>>n>>k;
bool flag=false;
int a[n];
for(int i=0;i<n;i++){
cin>>a[i];
if(a[i]==k){
    flag=true;
    break;
}
}
if(flag){
    cout<<"yes";

}
else{
    cout<<"no";
}
return 0;
}
