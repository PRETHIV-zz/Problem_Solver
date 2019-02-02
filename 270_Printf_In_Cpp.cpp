//average value of matrix
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
int n;
cin>>n;
float sum=0,avg,vl;
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        cin>>vl;
        sum+=vl;
    }
}
avg=sum/(n*n);
printf("%.6f",avg);
return 0;
}
