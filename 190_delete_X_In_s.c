//Back2rule
#include<stdio.h>
#include<string.h>
int main(){
char s[10000],x[10000],ans[10000];
scanf("%[^\n]s",s);
scanf("\n");
scanf("%[^\n]s",x);

char  *st,*e;
int sp,ep;
st=strstr(s,x);
sp=st-s;
ep=strlen(x)+sp-1;
int i;
static int k=0;
for(i=0;s[i]!='\0';i++){
        if(i>=sp&&i<=ep){
            continue;
        }
        else{
            ans[k++]=s[i];
        }
}
printf("%s",ans);
return 0;
}
