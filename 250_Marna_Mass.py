#Flipkart_Sum
n=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
#for i in range(n):
#   print("s",i,s[i])
#  print("f",i,f[i])
for i in range(n):
    m1=f[i]-s[i]
    for j in range(i+1,n):
        m2=f[j]-s[j]
        if m2<m1:
            tf=f[j]
            ts=s[j]
            f[j]=f[i]
            s[j]=s[i]
            f[i]=tf
            s[i]=ts
#print("*******")
#for i in range(n):
#    print("s",i,s[i])
#    print("f",i,f[i])
m1=min(s)
m2=max(f)
ans=[]
for i in range(m1,m2+1):
    ans.append(i)
#print(ans)
mc=0
for i in range(n):
    meet=True
    for j in range(s[i],f[i]):
        if j not in ans:
            meet=False
            break
        else:
            for k in range(len(ans)):
                if ans[k]==j:
                    ans[k]="#"
    if meet:
        mc+=1
print(mc)
