/*Prime nos between limit*/
#include<iostream>
using namespace std;
int main(){
	int l1,l2;
	cin>>l1>>l2;
	l1=l1+1;
	l2=l2-1;
	for(int j=l1;j<=l2;j++){
		
for(int i=2;i<=j;i++){
	if(j==1||j==0){
}
	else if(i==j){
		cout<<j<<" ";
	}
	else if(j%i==0){
		break;
	}
}
	}
	return 0;
}
