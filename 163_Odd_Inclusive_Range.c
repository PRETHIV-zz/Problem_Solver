//sum_Of_odd_inclusive
#include<stdio.h>
int main()
{
int n,k,s=0;
scanf("%d%d",&n,&k);
while(n<=k){if(n%2==1){s+=n;}n++;}
printf("%d",s);
return 0;
}
