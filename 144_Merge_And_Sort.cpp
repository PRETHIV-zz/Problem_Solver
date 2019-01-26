//Merge and sort
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
int m,n;
cin>>m>>n;
int a[m+n];
for(int i=0;i<m;i++){
    cin>>a[i];
}
for(int i=0;i<n;i++){
    cin>>a[m+i];
}
sort(a,a+m+n);
for(int i=0;i<m+n;i++){
    if(i==m+n-1){
        cout<<a[i];

    }
    else{
        cout<<a[i]<<" ";
    }

}
return 0;
}
