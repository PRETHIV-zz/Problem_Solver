//Smallest element check
#include<iostream>
#include<vector>
using namespace std;
int main()
{
int n;
cin>>n;
int a[n];
for(int i=0;i<n;i++)
{
    cin>>a[i];
}
vector<int> v;
for(int i=0;i<n-1;i++){
    if(a[i+1]<a[i])
    {
        v.push_back(a[i+1]);
    }
    else{
        v.push_back(-1);
    }
}v.push_back(-1);
for(int i=0;i<v.size();i++){
    if(i==v.size()-1){
        cout<<v[i];
    }
    else{
        cout<<v[i]<<" ";
    }
}
return 0;
}
