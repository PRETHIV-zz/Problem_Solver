//MIN Heap_In_Cpp
#include<bits/stdc++.h>
#include<iostream>
#include<vector>
using namespace std;
int main()
{
int n,k;
cin>>n>>k;
int val;
priority_queue<int,vector<int>,greater<int> > pq;
for(int i=0;i<n;i++)
{
    cin>>val;
    pq.push(val);
}
vector<int> v;
while(pq.empty()==false){
    v.push_back(pq.top());
    pq.pop();
}
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
