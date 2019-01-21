#include <stdio.h>
#include<string.h>
int main()
{
    char *s1,*s2;
    s1=malloc(10000);
    s2=malloc(10000);
    scanf("%s",s1);
    scanf("%s",s2);
    if(strstr(s1,s2)!=NULL){
        printf("yes");
        
    }
    else{
        
        printf("no");
    }
    free(s1);
    free(s2);
    return 0;
}
