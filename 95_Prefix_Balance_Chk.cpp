//Breathe cpp
#include<iostream>
#include<string>
int main(){
std::string s;
std::cin>>s;
int n=0,k=0;
for(int i=0;s[i]!='\0';i++){
    if(s[i]==')'){
    n++;
    }
    else if(s[i]=='('){
    k++;
    }
}
n==k?std::cout<<"yes":std::cout<<"no";
return 0;
}
