/*Prime nos between limit*/
#include<iostream>
#include<vector>
using namespace std;
int main(){
	vector<int> v;
	vector<int>::iterator b,e;
	int l1,l2;
	cin>>l1>>l2;
	l1=l1+1;
	l2=l2-1;
	
	for(int j=l1;j<=l2;j++){
		
for(int i=2;i<=j;i++){
	if(j==1||j==0){
}
	else if(i==j){
		v.push_back(j);
	}
	else if(j%i==0){
		break;
	}
}
	}
	e=v.end();
	for(b=v.begin();b!=e;b++){
		if(b==e-1){
			cout<<*b;
		}
		else{
			cout<<*b<<" ";
		}
	}
	return 0;
}
