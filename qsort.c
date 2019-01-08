#include <iostream>

using namespace std;
int compa(const void *,const void *);
int compa(const void *k,const void *l){
    return (*(int*)k-*(int*)l);
}
int main()
{
   int n;
   cin>>n;
   int a[n];
   for(int i=0;i<n;i++){
       cin>>a[i];
   }
   qsort(a,n,sizeof(int),compa);
   for(int i=0;i<n;i++){
       if(i==n-1){
           cout<<a[i];
       }
       else{
           cout<<a[i]<<" ";
       }
   }
   return 0;
}
