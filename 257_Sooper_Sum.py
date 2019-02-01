#min dist u v
n=int(input())
a=list(map(int,input().split()))
u,v=map(int,input().split())
#forward check
ans=[]
for i in range(len(a)):
    if a[i]==u:
        c=0
        for j in range(i+1,len(a)):
            c+=1
            if a[j]==v:
                ans.append(c)
                break
for i in range(len(a)-1,-1,-1):
    if a[i]==u:
        c=0
        for j in range(i-1,-1,-1):
            c+=1
            if a[j]==v:
                ans.append(c)
                break
print(min(ans))
