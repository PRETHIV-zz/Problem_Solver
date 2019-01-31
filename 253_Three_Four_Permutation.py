#34nnos
ans=[3,4,33,34,43,44]
q=[33,34,43,44]
n=int(input())
on=n
while len(ans)<=on:
    a=[]
    for i in range(3,5):
        for ii in q:
            s=str(i)+str(ii)
            s=int(s)
            a.append(s)
            ans.append(s)
    q=a.copy()
print(ans[n-1])
