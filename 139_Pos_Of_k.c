//hlo guvi
#include<stdio.h>
int main()
{
int n,k;
scanf("%d%d",&n,&k);
int a[n],i,l,f=1;
for(i=0;i<n;i++){

    scanf("%d",&a[i]);
    if(a[i]==k&&f==1){l=i+1;
    f=0;
    }
}
printf("%d",l);
return 0;
}
