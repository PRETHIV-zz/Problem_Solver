#include <stdio.h>

int main()
{
char s1[10000],s2[10000];
int i,l1=0,l2=0;
scanf("%s%s",s1,s2);
for(i=0;s1[i]!='\0';i++)
{
    l1++;
    
}
for(i=0;s2[i]!='\0';i++)
{
    l2++;
}
if(l1!=l2)
{
    printf("no");
    
}
else{
    int val=0;
    for(i=0;i<l1;i++)
    {
        if(s1[i]==s2[i]||(s1[i]-s2[i])==32||(s1[i]-s2[i])==-32)
        {
            val++;
        }
    }
    if(val==l2)
    {
        printf("yes");
    }
    else{
        printf("no");
    }
}
return 0;
}
