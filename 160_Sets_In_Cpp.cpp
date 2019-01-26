//cppsets
#include<set>
#include<iostream>
#include<vector>
using namespace std;
int main(){
set<int> s;
vector<int> v;
int n;
cin>>n;
int on=n;
while(on>0){
    s.insert(on%10);
    v.push_back(on%10);
    on=on/10;
}
int len=s.size();
int flag=0;
for(set<int>::iterator i=s.begin();i!=s.end();i++){
    int c=-1;
    for(int j=0;j<v.size();j++){
        if(*i==v[j]){
            c++;
        }
    }
    if(c>0){flag=1;}
}
if(flag==1){
cout<<"yes";
}
else{
cout<<"no";
}
return 0;
}
