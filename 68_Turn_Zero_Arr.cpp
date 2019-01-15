#include<iostream>
using namespace std;
int main(){
int r,c;
cin>>r>>c;
int a[r][c],b[r][c];
for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
        cin>>a[i][j];
        b[i][j]=1;
    }
}
for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
        if(a[i][j]==0){
            for(int ii=0;ii<c;ii++){
            b[i][ii]=0;
            }
            for(int jj=0;jj<r;jj++){
            b[jj][j]=0;
            }
        }
    }
}
for(int i=0;i<r;i++){
for(int j=0;j<c;j++){
        if(j==c-1){
            cout<<b[i][j];
        }
        else{
    cout<<b[i][j]<<" ";
    }
}
cout<<endl;
}
return 0;
}
