//Hunting started
#include<stdio.h>
int main()
{
int n,k;
scanf("%d%d",&n,&k);
int i=0,a[n],ans[n];
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
for(i=0;i<n;i++){
    ans[i]=a[(i+k)%n];
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
