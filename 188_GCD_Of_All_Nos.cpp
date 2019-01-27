//gcd
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
int n;
cin>>n;
int a[n],m;
for(int i=0;i<n;i++){
    cin>>a[i];
    if(i==0){m=a[0];}
    if(m<a[i]){m=a[i];}
}
int i=1;
int gcd;
while(i<=m){
    int c=0;
    for(int k=0;k<n;k++){if(a[k]%i==0){c++;}}
    if(c==n){ gcd=i; }
    i++;

}
cout<<gcd;

return 0;
}
