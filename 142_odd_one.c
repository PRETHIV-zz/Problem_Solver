//odd one
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n],i;
int of=0,ef=0,ol=0,el=0;
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
    if(a[i]%2==0){
        ef++;
        el=i;
    }
    else{
        of++;
        ol=i;
    }
}
if(ef==1){
    printf("%d",a[el]);
}
else if(of==1){
    printf("%d",a[ol]);
}
return 0;
}
