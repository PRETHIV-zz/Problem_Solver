//maxof bw or of all seg
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n],i;
int ans[n];
for(i=0;i<n;i++){
scanf("%d",&a[i]);
ans[i]=0;
}

int j;
static int k=0;
for(i=0;i<n;i++){
        ans[i]=a[i];
    for(j=0;j<n;j++){
        if(i!=j){
            ans[i]=ans[i]|a[j];
        }
    }
}
int m=ans[0];
for(i=0;i<n;i++){
if(ans[i]>m){
    m=ans[i];
}
}
printf("%d",m);
return 0;
}
