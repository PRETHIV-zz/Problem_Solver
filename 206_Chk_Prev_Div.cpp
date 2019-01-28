#include <iostream>
#include<utility>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
   int n,val;
   cin>>n;
   vector<int> v,ans;
   for(int i=0;i<n;i++){
       cin>>val;
       v.push_back(val);
   }
   for(int i=1;i<n;i++){
       if(v[i]%v[i-1]==0){
       ans.push_back(v[i]);
           
       }
   }
   for(int i=0;i<ans.size();i++){
       if(i==ans.size()-1){
           cout<<ans[i];
       }
       else{
           cout<<ans[i]<<" ";
       }
   }
   return 0;
}
