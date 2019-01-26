//biwiseor
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int i,a[n];
for(i=0;i<n;i++){
    scanf("%d",&a[i]);

}
int ans=a[0];
for(i=1;i<n;i++){
    ans=ans|a[i];
}
printf("%d",ans);
return 0;
}
