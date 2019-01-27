//No_Of_Occurence_In_Decreasing
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
bool sortbysec(const pair<int,int> &a,const pair<int,int> &b){return (a.second<b.second);}
int main()
{
int n;
cin>>n;
vector<int> v;
set<int> s;
vector< pair<int,int> > sf;
for(int i=0;i<n;i++){
    int val;
    cin>>val;
    v.push_back(val);
    s.insert(val);
}
set<int>::iterator ii,j;
ii=s.begin();
j=s.end();
while(ii!=j){
    int c=0;
    for(int i=0;i<n;i++){
        if(*ii==v[i]){
            c++;
        }
    }
    sf.push_back(make_pair(*ii,c));
    ii++;
}
sort(sf.begin(),sf.end());
sort(sf.begin(),sf.end(),sortbysec);
for(int i=sf.size();i>0;i--){
    if(i==1){
        cout<<sf[i-1].first;
    }
    else{
        cout<<sf[i-1].first<<" ";
    }
}

return 0;
}
