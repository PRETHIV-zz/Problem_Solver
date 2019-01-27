//printallnosinsorted
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
int main()
{
int n,k;
cin>>n>>k;
int a[n];
set<int> s;
vector<int> ans;
for(int i=0;i<n;i++){
    cin>>a[i];
    s.insert(a[i]);
}
vector< pair<int,int> > ss;
set<int>::iterator sb,se;
se=s.end();
for(sb=s.begin();sb!=se;sb++){
    int c=0;
    for(int i=0;i<n;i++){
        if(*sb==a[i]){c++;}
    }
    ss.push_back(make_pair(c,*sb));
}
for(int i=0;i<ss.size();i++){
    if(ss[i].first<k){
        ans.push_back(ss[i].second);
        }
}
sort(ans.begin(),ans.end());
for(int i=0;i<ans.size();i++){
    if(i==ans.size()-1){cout<<ans[i];}
    else{cout<<ans[i]<<" ";}
}
return 0;
}
