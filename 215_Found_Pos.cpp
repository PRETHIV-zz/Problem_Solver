#include<iostream>
#include<utility>
#include<vector>
using namespace std;
pair<int,int> pickeve(vector< pair<int,int> > v){
    vector< pair<int,int> > e;
    for(int i=0;i<v.size();i++){
        if((i+1)%2==0){
            e.push_back(v[i]);
        }
    }
    if(e.size()==1){
        return e[0];
    }
    else{
        return pickeve(e);
    }
}
int main(){
int n;
cin>>n;
vector< pair<int,int> > v;
for(int i=0;i<n;i++){
    int val;
    cin>>val;
    v.push_back(make_pair(i,val));
}
pair<int,int> ans;
ans=pickeve(v);
cout<<ans.first;
return 0;
}
