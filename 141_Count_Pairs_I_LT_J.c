//love c
#include<stdio.h>
int main()
{
int c=0;
int n;
scanf("%d",&n);
int a[n],i,j;
for(i=0;i<n;i++){

    scanf("%d",&a[i]);
}
for(i=0;i<n;i++){
    for(j=0;j<n;j++){
        if(a[i]<a[j]){
            c++;
        }
    }

}
printf("%d",c);
return 0;
}
