//hlo guvi again ah
#include<stdio.h>
int main(){
int n;
scanf("%d",&n);
int ic=0;
int a[n+2][n+2];
int i,j;
for(i=0;i<n+2;i++){
    for(j=0;j<n+2;j++){
        a[i][j]=0;
    }
}
for(i=1;i<=n;i++){
    for(j=1;j<=n;j++){
        scanf("%d",&a[i][j]);
    }
}
for(i=1;i<=n;i++){

    for(j=1;j<=n;j++){
        int x[8],y[8];
        x[0]=i-1;
        y[0]=j-1;
        x[1]=i-1;
        y[1]=j;
        x[2]=i-1;
        y[2]=j+1;
        x[3]=i;
        y[3]=j-1;
        x[4]=i;
        y[4]=j+1;
        x[5]=i+1;
        y[5]=j-1;
        x[6]=i+1;
        y[6]=j;
        x[7]=i+1;
        y[7]=j+1;
        int c=0;
        int ii;
        for(ii=0;ii<8;ii++){
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
printf("%d",ic);
return 0;
}
