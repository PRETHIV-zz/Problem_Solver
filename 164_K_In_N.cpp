//power_Of_cpp
#include<iostream>
#include<vector>
using namespace std;
int main()
{
vector<int> a,b;
int n,k,on;
cin>>n>>k;
on=n;
while(on>0){a.push_back(on%10); on/=10;}
for(int i=0;i<=k;i++){
    for(int j=0;j<a.size();j++){
        if(i==a[j]){b.push_back(i); break;}
    }
}
if(b.size()==k+1){cout<<"yes";}
else{cout<<"no";}
return 0;
}
