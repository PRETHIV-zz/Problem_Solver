//Pnt lies on a same line
#include<stdio.h>
int main(){
int x1,x2,x3,y1,y2,y3;
scanf("%d%d",&x1,&y1);
scanf("%d%d",&x2,&y2);
scanf("%d%d",&x3,&y3);
if(x1==x2&&1==x3){
printf("yes");
}
else if(y1==y2&&1==y3){
printf("yes");
}
else{
printf("no");
}
return 0;
}
