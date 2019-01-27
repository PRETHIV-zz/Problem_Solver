//another_Set
#include<iostream>
#include<set>
using namespace std;
int main()
{
int n,m;
set<int> s;
cin>>n>>m;
for(int i=0;i<m+n;i++){
    int a;
    cin>>a;
    s.insert(a);
}
for(set<int>::iterator b=s.begin();b!=s.end();b++){
    cout<<*b<<" ";
}

return 0;
}
