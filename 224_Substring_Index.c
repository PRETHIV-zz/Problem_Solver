#include <stdio.h>
#include<string.h>
int main()
{
    char s1[100000],s2[100000];
    scanf("%[^\n]s",s1);
    scanf("\n");
    scanf("%[^\n]s",s2);
    char *p;
    int pos;
    p=strstr(s1,s2);
    if(p!=NULL){
        pos=p-s1;
        printf("%d",pos);
        
    }
    else{
        printf("-1");
    }
    return 0;
}
