//Back2C
#include<stdio.h>
int main(){
int l,r;
scanf("%d%d",&l,&r);
int c=r;
while(1){
    if(c%l==0&&c%r==0){
        printf("%d",c);
        break;
    }
    c++;
}
return 0;
}
