//Divide both
#include<stdio.h>
int main(){
int n,k;
scanf("%d%d",&n,&k);
int l=k;
while(l>=1){
if(n%l==0&&k%l==0){
printf("%d",l);
break;
}
l--;
}
return 0;
}
