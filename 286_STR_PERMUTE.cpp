//permutation of a string
#include<iostream>
#include<string>
#include<algorithm>
#include<set>
using namespace std;
set<string> ans;
void permute(string in,string out)
{
    if(in==""){
        ans.insert(out);
    }
    else{
        for(int i=0;i<in.size();i++){
            permute(in.substr(1),out+in[0]);
            rotate(in.begin(),in.begin()+1,in.end());
        }
    }
}

int main()
{
string s;
cin>>s;
permute(s,"");
set<string>::iterator b,e;
b=ans.begin();
e=ans.end();
while(b!=e){
    cout<<*b<<endl;
    b++;
}
return 0;
}
