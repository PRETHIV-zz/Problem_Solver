//revers_string
#include<string>
#include<iostream>
using namespace std;
int main()
{
string s,ss="";
cin>>s;
int l=0;
for(int i=0;s[i]!='\0';i++){l++;}
for(int i=l-1;i>=0;i--){
    if(i!=0){
    ss=ss+s[i]+"-";}
    else{
        ss=ss+s[i];
    }
}

cout<<ss;
return 0;
}
