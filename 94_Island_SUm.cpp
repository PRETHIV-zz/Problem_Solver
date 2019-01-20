#include<iostream>
#include<vector>
/*It is going to be my favourite sum ever i had attended in guvi*/
using namespace std;
int main(){
int n;
cin>>n;
int ic=0;
int a[n+2][n+2];
for(int i=0;i<n+2;i++){
    for(int j=0;j<n+2;j++){
        a[i][j]=0;
    }
}
for(int i=1;i<=n;i++){
    for(int j=1;j<=n;j++){
        cin>>a[i][j];
    }
}
for(int i=1;i<=n;i++){

    for(int j=1;j<=n;j++){
        vector<int> x,y;
        x.push_back(i-1);
        y.push_back(j-1);
        x.push_back(i-1);
        y.push_back(j);
        x.push_back(i-1);
        y.push_back(j+1);
        x.push_back(i);
        y.push_back(j-1);
        x.push_back(i);
        y.push_back(j+1);
        x.push_back(i+1);
        y.push_back(j-1);
        x.push_back(i+1);
        y.push_back(j);
        x.push_back(i+1);
        y.push_back(j+1);
        int c=0;
        for(int ii=0;ii<8;ii++){
            if(a[i][j]==1&&a[x[ii]][y[ii]]==0){
                c+=1;
            }
            else{
                break;
            }
        }
        if(c==8){
            ic++;
        }
    }
}
cout<<ic;
return 0;
}
