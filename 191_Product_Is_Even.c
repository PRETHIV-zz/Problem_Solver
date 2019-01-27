//Born2Rule
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n],i;
int ans=1;
for(i=0;i<n;i++){
scanf("%d",&a[i]);
ans*=a[i];
}
if(ans%2==0){ printf("even");}
else{printf("odd");}

return 0;
}
