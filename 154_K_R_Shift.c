//l_shift
#include<stdio.h>
int main(){
int n;
int k;
scanf("%d%d",&n,&k);
float ans;
ans=n>>k;
printf("%.2f",ans);
return 0;
}
