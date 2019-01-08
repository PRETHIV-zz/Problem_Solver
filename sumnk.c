/*It is my own code guvi*/
#include<stdio.h>
int main(){
int n,k;
scanf("%d",&n);
scanf("%d",&k);
int a[n],sum=0;
for(int i=0;i<n;i++){
  scanf("%d",&a[i]);
  if(i<k){
  sum+=a[i];
  }
}
printf("%d",sum);
return 0;
}
