#Delete one cons digs
n=input()
ans=[]
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        s=n[0:i]+n[i+1:]
        ans.append(int(s))
print(max(ans))
