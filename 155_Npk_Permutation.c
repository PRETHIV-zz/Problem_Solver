//NPK_Permutation
#include<stdio.h>
int pretfact(int n){
    if(n==0){
        return 1;
    }
    else{
        return n*pretfact(n-1);
    }
}
int main()
{
int n,k;
scanf("%d%d",&n,&k);
int num,den;
num=pretfact(n);
den=pretfact(n-k);
printf("%d",num/den);
return 0;
}
