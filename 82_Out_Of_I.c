//kya reh Tough probs ah
#include<stdio.h>
int main(){
int n;
scanf("%d",&n);
int a[n];
int i;
for(i=0;i<n;i++){
scanf("%d",&a[i]);
}
int j;
for(i=0;i<n;i++){
    int ans=1;
    for(j=0;j<n;j++){
        if(i!=j){
            ans*=a[j];
        }
    }
    if(i==n-1){
    printf("%d",ans);}
    else{
    printf("%d ",ans);
    }
}
return 0;
}
