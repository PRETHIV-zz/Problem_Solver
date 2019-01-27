//sum_Of_Sums
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n],i;
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
int s=0;
for(i=0;i<n-1;i++){
    s+=a[i]+a[i+1];

}
printf("%d",s);
return 0;
}
