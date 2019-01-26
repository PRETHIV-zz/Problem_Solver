//backingup2c
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n],ans[n];
int i,j;
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
int lim=n;
if(n%2==1){
    lim=n-1;
    ans[n-1]=a[n-1];
}
for(i=0;i<lim;i=i+2){
    ans[i+1]=a[i];
    ans[i]=a[i+1];
}

for(i=0;i<n;i++){
    if(i==n-1){
        printf("%d",ans[i]);
    }
    else{
        printf("%d ",ans[i]);
    }
}
return 0;
}
