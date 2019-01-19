//N_K_Insertion
#include<iostream>
#include<vector>
using namespace std;
int pret(vector<int> a){
int m=a[0];
vector<int>::iterator b,e;
b=a.begin();
e=a.end();
while(b!=e){

    if(*b>m){

        m=*b;
    }
b++;
}
return m;
}

int main(){
int n,k;
cin>>n>>k;
vector<int> a;
for(int i=0;i<n;i++){
int kk;
cin>>kk;
a.push_back(kk);
}
vector<int> ans;
for(int i=0;i<k;i++){
    int nn;
    cin>>nn;
    a.push_back(nn);
    if(i==k-1){

        cout<<pret(a);
    }
    else{

        cout<<pret(a)<<" ";
    }
}
return 0;
}
