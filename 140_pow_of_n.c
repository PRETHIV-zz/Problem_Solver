//pow of n
#include<stdio.h>
int main()
{
int b,p;
scanf("%d%d",&b,&p);
int a=1;
while(p>=1){
a*=b;
p--;
}
printf("%d",a);
return 0;
}
