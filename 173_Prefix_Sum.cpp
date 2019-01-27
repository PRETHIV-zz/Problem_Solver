//prefix_SUm_Array
#include<iostream>
#include<vector>
using namespace std;
int main()
{
int n;
cin>>n;
int a[n],s=0;
for(int i=0;i<n;i++){
    cin>>a[i];
}
for(int i=0;i<n;i++){
    s+=a[i];
    if(i==n-1){
        cout<<s;
    }
    else{
        cout<<s<<" ";
    }
}



return 0;
}
