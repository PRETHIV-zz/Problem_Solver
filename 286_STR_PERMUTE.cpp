//permutation of a string
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
void permute(string in,string out)
{
    if(in==""){
        cout<<out<<endl;
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
return 0;
}
