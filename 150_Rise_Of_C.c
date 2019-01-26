//Maximum of and of all seg
#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n],i;
int df[n],j;
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
    df[i]=0;
}

for(i=0;i<n;i++){
    df[i]=a[i];
    for(j=i+1;j<n;j++){
        df[i]=df[i]&a[j];
    }

}
int m=df[0];
for(i=0;i<n;i++){
    if(df[i]>m){
        m=df[i];
    }
}
printf("%d",m);
return 0;
}
