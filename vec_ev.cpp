#include<iostream>
#include<vector>
using namespace std;
int main(){
	vector<int> v;
	int l1,l2;
	cin>>l1>>l2;
	l1++;
	for(int i=l1;i<l2;i++){
		if(i%2==0){
			v.push_back(i);
		}
	}
	vector<int>::iterator b,e;
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
