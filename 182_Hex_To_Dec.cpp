//hex_to_dec
#include<iostream>
#include<string>
using namespace std;
int pretpow(int b,int p){
    long long int ans=1;
    if(p==0){return ans;}
    else{
        while(p>=1){
            ans*=b;
            p--;
        }
        return ans;
    }
}
int findnum(char c){
    if(c-48>=0 and c-48<=9){
        return (c-48);
    }
    else{
        int v=10;
        for(char cc='A';cc<='F';cc++){
            if(c==cc){return v;}
            v++;
        }
    }
}
int main(){
string s;
cin>>s;
int l=0;
long long int dec=0;
string rev="";
for(int i=0;s[i]!='\0';i++){l++;}
for(int i=l-1;i>=0;i--){rev=rev+s[i];}
for(int i=0;rev[i]!=0;i++){ int val=findnum(rev[i]); dec=dec+(val*(pretpow(16,i)));}
cout<<dec;
return 0;
}
