/*It is my own code guvi*/
#include<iostream>
using namespace std;
int main(){
int n;
cin>>n;
int i;
if(n==1||n==0){
	cout<<"no";
}
else{
for(i=2;i<=n;i++){
	if(i==n){
		cout<<"yes";
	}
	else if(n%i==0){
		cout<<"no";
		break;
	}
}
}
return 0;
}
