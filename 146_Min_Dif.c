//Max_Dif
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int a[n],i;
    for(i=0;i<n;i++){
    scanf("%d",&a[i]);
    }
    int df[n*n],j;
    static int k=0;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
                if(i!=j){
            df[k++]=abs(a[i]-a[j]);

        }}
    }
    int m=df[0];
    for(i=0;i<(n*n)-n;i++){
        if(df[i]<m&&df[i]!=0){
            m=df[i];
        }
    }
    printf("%d",m);
return 0;
}
