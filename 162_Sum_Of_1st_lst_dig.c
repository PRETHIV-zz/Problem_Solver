//KING_OF_JUNGLE_C
#include<stdio.h>
int main()
{
int n,s=0,rev=0;
scanf("%d",&n);
s+=n%10;
while(n>0){ rev=rev*10+(n%10); n/=10; }
s+=rev%10;
printf("%d",s);
return 0;
}
