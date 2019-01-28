#include <iostream>
#include<utility>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
   int n,val;
   cin>>n;
   vector< pair<int,int> > v;
   for(int i=0;i<n;i++){
       cin>>val;
       v.push_back(make_pair(0,val));
   }
   for(int i=0;i<n;i++){
       cin>>val;
       v[i].first=val;
   }
   sort(v.begin(),v.end());
   for(int i=0;i<n;i++){
       if(i==n-1){
           cout<<v[i].second;
       }
       else{
           cout<<v[i].second<<" ";
       }
   }
   return 0;
}
