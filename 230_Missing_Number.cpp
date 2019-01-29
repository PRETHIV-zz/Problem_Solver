#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
int n;
cin>>n;
int a[n],sum=0;
set<int> s;
for(int i=0;i<n;i++){
    cin>>a[i];
    sum+=a[i];
    s.insert(a[i]);
}
set<int>::iterator b,e;
b=s.begin();
e=s.end();
int two_sum=0;
while(b!=e){
    two_sum+=*b;
    b++;
}

cout<<2*two_sum-sum;
return 0;
}
