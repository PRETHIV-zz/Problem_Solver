#include<iostream>
#include<utility>
#include<algorithm>
using namespace std;
int main()
{
int n;
cin>>n;
int a[n],m;
for(int i=0;i<n;i++){
    cin>>a[i];
}
m=abs((a[0]+a[1])-0);
pair<int,int> ans;
ans=make_pair(a[0],a[1]);
for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
        int val;
        val=abs((a[i]+a[j])-0);
        if(val<m){
            m=val;
            ans.first=a[i];
            ans.second=a[j];
        }
    }
}
cout<<ans.first<<" "<<ans.second;
return 0;
}
