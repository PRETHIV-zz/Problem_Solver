//set_Already_know
#include<iostream>
#include<vector>
#include<set>
using namespace std;
int main()
{
int n;
cin>>n;
int a;
set<int> s;
for(int i=0;i<n;i++){
    cin>>a;
    s.insert(a);

}
vector<int> v;
for(set<int>::iterator b=s.begin();b!=s.end();b++)
{
    v.push_back(*b);
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
