//hlo guvi
#include<iostream>
using namespace std;
int main()
{
int n;
cin>>n;
int a[n];
for(int i=0;i<n;i++){
    cin>>a[i];
}
int l=0;
for(int i=1;i<n-1;i++){
    if(a[i]>a[i-1]&&a[i]>a[i+1]){
        l=i;
        break;
    }

}
int m=a[0];
for(int i=0;i<=l;i++){
    if(m<a[i]){
        m=a[i];
    }
}
cout<<m;
return 0;
}
