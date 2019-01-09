#include <stdio.h>

int main()
{
    int a=0,b=1,sum=0;
    int n;
    scanf("%d",&n);
    int i;
    for(i=0;i<n;i++){
        sum=a+b;
        if(i==0){
            printf("1 ");
            n--;
        }
        if(i==n-1){
        printf("%d",sum);
        }
        else{
        printf("%d ",sum);
        }
        a=b;
        b=sum;
    }
    return 0;
}
