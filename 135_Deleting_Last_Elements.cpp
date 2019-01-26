//hlo guvi
#include<iostream>
#include<vector>
using namespace std;
int main()
{
int n,k;
cin>>n>>k;
vector<int> a;
int e;
for(int i=0;i<n;i++){
    cin>>e;
    a.push_back(e);
}
for(int i=0;i<k;i++){
    a.pop_back();
}
for(int i=0;i<n-k;i++){
    if(i==n-k-1){
        cout<<a[i];
    }
    else{
        cout<<a[i]<<" ";
    }

}
return 0;
}
