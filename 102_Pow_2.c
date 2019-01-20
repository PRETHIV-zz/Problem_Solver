//chk_Pow2
#include<stdio.h>
int main(){
int n;
scanf("%d",&n);
int on,c=0;
on=n;
while(n>0){
    n=n/2;
    c++;
}
int ans=1,i;
for(i=0;i<c-1;i++){
    ans*=2;
}
if(ans==on){
    printf("yes");

}
else{
    printf("no");
}
return 0;
}
