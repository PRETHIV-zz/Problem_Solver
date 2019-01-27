//Maximum_Odd_Even
#include<iostream>
#include<vector>
using namespace std;
int main()
{
int n;
cin>>n;
vector<int> v;
int on=n,rev=0,orev;
while(on>0){
    rev=rev*10+(on%10);
    on=on/10;
}
orev=rev;
while(rev>0){
    if(rev%2==0){
    v.push_back(0);}
    else{
        v.push_back(1);
    }
    rev/=10;
}
int c=1,m=0;
for(int i=0;i<v.size()-1;i++){
    if(v[i]==0&&v[i+1]==1||v[i]==1&&v[i+1]==0){
        c+=1;
        if(m<c){
        m=c;}
    }
    else{
        c=0;
    }

}
cout<<m;
return 0;
}
