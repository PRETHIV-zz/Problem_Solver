/*It is my code guvi*/
#include<stdio.h>
int main(){
int b,e;
scanf("%d",&b);
scanf("%d",&e);
int ans=1;
while(e>=1){
ans*=b;
e--;
}
printf("%d",ans);
return 0;
}
