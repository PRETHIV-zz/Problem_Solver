//finding_Prime
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool pretprime(int n){
    for(int i=2;i<=n;i++){
        if(i==n){
            return true;
        }
        else if(n%i==0){
            return false;
        }
    }

}
int main()
{
int n;
cin>>n;
vector<int> v;
for(int i=2;i<=n;i++)
{
    if(pretprime(i)&&(n%i)==0){
        v.push_back(i);
    }
}
sort(v.begin(),v.end());
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
