//l_shift
#include<stdio.h>
int main(){
int n,k;
scanf("%d%d",&n,&k);
n=n>>k;
printf("%d",n);
return 0;
}
