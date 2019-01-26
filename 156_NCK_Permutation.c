//NCK_Combinations
#include<stdio.h>
int main()
{
int n,k;
scanf("%d%d",&n,&k);
int num=1,den=1;
int tn,tk;
tn=n;
tk=k;
while(tk>=1){
    num=num*tn;
    tn--;
    tk--;
}
tn=n;
tk=k;
while(tk>=1){
    den=den*tk;
    tk--;
}
if(k==0){
    num=n;
    den=1;
}
printf("%d",num/den);
return 0;
}
