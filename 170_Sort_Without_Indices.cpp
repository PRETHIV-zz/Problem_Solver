//print_elem_And_ind
#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
using namespace std;
int main()
{
int n;
cin>>n;
int a;
vector< pair <int,int> > v;
for(int i=0;i<n;i++){
    cin>>a;
    v.push_back(make_pair(a,i+1));
}
sort(v.begin(),v.end());
for(int i=0;i<n;i++){
    if(i==n-1){
        cout<<v[i].second;
    }
    else{
        cout<<v[i].second<<" ";
    }
}

return 0;
}
