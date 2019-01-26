//BW_XOR_Array
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n],ans,i;
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
ans=a[0];
for(i=1;i<n;i++){
    ans=ans^a[i];
}
printf("%d",ans);
return 0;
}
