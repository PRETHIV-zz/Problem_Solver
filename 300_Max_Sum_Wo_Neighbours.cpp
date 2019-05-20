#include<iostream>

using namespace std;

int pmax(int a,int b){
    if(a>b){return a;}
    else{return b;}
}

int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int inc,exc,enew;
    inc=a[0];
    exc=0;
    for(int i=1;i<n;i++)
    {
        enew=pmax(inc,exc);
        inc=exc+a[i];
        exc=enew;
    }

    cout<<pmax(inc,exc);
    return 0;
}
