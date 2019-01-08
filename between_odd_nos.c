//it is my own code guvi
#include<stdio.h>
int main(){
	int i,k;
	scanf("%d",&i);
	scanf("%d",&k);
	int j,l=k-1;
	for(j=i+1;j<=l;j++){
		if(j%2==1){
			printf("%d ",j);
		}
	}
	return 0;
}
