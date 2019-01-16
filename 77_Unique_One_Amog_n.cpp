#include<iostream>
using namespace std;
int main(){
int n;
cin>>n;
int a[n],f=0;
for(int i=0;i<n;i++){
    cin>>a[i];
}
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        if(a[i]==a[j]){
            f+=1;
        }
    }
    if(f==1){
        cout<<a[i];
        break;
    }
    f=0;
}
return 0;
}
