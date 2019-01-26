//Back2c
#include<stdio.h>
int main(){
int n,k,p;
scanf("%d%d%d",&n,&k,&p);
int on=n,c=0,rev=0;
while(on>0){ c++; rev=rev*10+(on%10); on/=10;}
on=n;
int a[c],kk=0;
while(rev>0){a[kk++]=rev%10; rev/=10;}
printf("%d",a[k+p-1]);
return 0;
}
