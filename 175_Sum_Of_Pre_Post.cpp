//sum_Of_Pre_Post
//prefix_SUm_Array
#include<iostream>
#include<vector>
using namespace std;
int main()
{
int n;
cin>>n;
int a[n],s=0,sum=0;
vector<int> vpre,vpost,v;
for(int i=0;i<n;i++){
    cin>>a[i];
    sum+=a[i];
     v.insert(v.begin(),a[i]);
}
for(int i=0;i<n;i++){
    s+=a[i];
    vpre.push_back(s);
    vpost.push_back(sum);
    sum-=v[i];
}
for(int i=0;i<n;i++){
if(i==n-1){
    cout<<vpre[i]+vpost[i];
}
else{
    cout<<vpre[i]+vpost[i]<<" ";
}
}


return 0;
}
