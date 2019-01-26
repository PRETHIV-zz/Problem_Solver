//Length_Of_Continuos
//Welcome Stalkers
int main()
{
int n;
scanf("%d",&n);
int a[n],i,l[n],j;
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
for(i=0;i<n;i++){
    int c=0;
    for(j=i;j<n-1;j++){
        if(a[j]<a[j+1]){
            c++;
          //  printf("\n %d %d ",a[j],a[j+1]);
        }
        else{
            break;
        }
    }
    l[i]=c+1;

}


int m=l[0];

for(i=0;i<n;i++){
    if(m<l[i]){
        m=l[i];
    }

}
printf("%d",m);
return 0;
}
