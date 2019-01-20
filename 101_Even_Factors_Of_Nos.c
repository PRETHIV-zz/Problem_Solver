//even_factors_of_nos
struct node{
    int data;
    struct node *next;
};
#include<stdio.h>
int main(){
int n;
scanf("%d",&n);
int i;
struct node *head=malloc(sizeof(struct node));
int c=0;
struct node *cur;
cur=head;
for(i=2;i<=n;i++){
    if(n%i==0&&i%2==0){
        if(c==0){
            head->data=i;
            c++;
        }
        else{
            cur->next=malloc(sizeof(struct node));
            cur=cur->next;
            cur->data=i;
        }
    }
}
cur->next=NULL;
struct node *p;
p=head;
while(p!=0){
    if(p->next==0){
        printf("%d",p->data);
        break;
    }
    else{
        printf("%d ",p->data);
        p=p->next;
    }
}
return 0;
}
