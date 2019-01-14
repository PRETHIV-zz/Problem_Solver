# Hello World program in Python
#guvi iam prethiv
n=int(input())
l1=list(map(int,input().split(" ")))
l2=l1.copy()
ans=0
cnt=0
ch=0
for i in range(len(l1)):
    tempcnt=0
    for j in range(i+1,len(l2),1):
        tempcnt+=1
        if l1[i]==l2[j]:
            if tempcnt<cnt or ch==0:
                ch=1
                cnt=tempcnt
                ans=l1[i]
print(ans)
