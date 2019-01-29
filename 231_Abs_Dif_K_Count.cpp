#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
int n,k;
cin>>n>>k;
int c=0;
int a[n];
for(int i=0;i<n;i++){
    cin>>a[i];
}
for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
        if(abs(a[i]-a[j])==k){
        c++;
        }
    }
}
cout<<c;
return 0;
}
