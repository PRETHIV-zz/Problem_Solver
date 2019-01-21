//N_Is_A_Pow_Of_K
#include<iostream>
using namespace std;
int main()
{
int n,k;
cin>>n>>k;
int ans=1,pow=0;
int on=n;
while(n>0){
    n=n/k;
    pow++;
}
for(int i=0;i<pow-1;i++){
    ans*=k;
}

if(ans==on){
    cout<<"yes";
}
else{
    cout<<"no";
}
return 0;
}
