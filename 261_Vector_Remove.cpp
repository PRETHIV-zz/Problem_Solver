//Back2form
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
int n,k;
cin>>n>>k;
vector<int> v;
for(int i=0;i<n;i++){
    int val;
    cin>>val;
    if(val!=k){
        v.push_back(val);
    }

}
if(v.size()==0){
    cout<<"empty";
}
else{
for(int i=0;i<v.size();i++){
    if(i==v.size()-1){
        cout<<v[i];
    }
    else{
        cout<<v[i]<<" ";
    }
}
}
return 0;
}
