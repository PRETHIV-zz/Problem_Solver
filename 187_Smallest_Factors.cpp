//smallst facctor
#include<iostream>
using namespace std;
bool chkfact(int no,int f){
    if(no%f==0){return true;}
    else{return false;}
}
int main(){
int n;
cin>>n;
int a[n];
for(int i=0;i<n;i++){
    cin>>a[i];
}
int i=1;
while(true){
    int c=0;
    for(int j=0;j<n;j++){
        if(chkfact(i,a[j])){
            c++;
        }
    }
    if(c==n){
        break;
        }
        i++;
}
cout<<i;
return 0;
}
