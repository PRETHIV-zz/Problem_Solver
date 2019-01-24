#hlo guvi i am pret
n,k=map(int,input().split())
ans=[]
al=[]
a=list(map(int,input().split()))
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    ans.append(c)
for i in range(len(ans)):
    if ans[i]==k:
        al.append(a[i])
allli=list(set(al))
for i in range(len(allli)):
    if i==len(allli)-1:
        print(allli[i],end="")
    else:
        print(allli[i],end=" ")
