//prefix_SUm_Array
#include<iostream>
#include<vector>
using namespace std;
int main()
{
int n;
cin>>n;
int s=0;
int a;
vector<int> v;
for(int i=0;i<n;i++){
    cin>>a;
    v.insert(v.begin(),a);
    s+=a;
}
for(int i=0;i<n;i++){

    if(i==n-1){
        cout<<s;
    }
    else{
        cout<<s<<" ";
    }
    s-=v[i];
}



return 0;
}
