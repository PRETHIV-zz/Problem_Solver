#Flipkart_Sum
#Plz upgrade ur checking system dont consider last space trim and compare we r loosing lots of points on this basis only
#or else plz specify in the questionthat an empty space is to be printed at the end
n=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
#for i in range(n):
#   print("s",i,s[i])
#  print("f",i,f[i])
for i in range(n-1):
    m1=f[i]-s[i]
    for j in range(0,n-i-1):
        m2=f[j]-s[j]
        if m2>m1:
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
    q=[]
    for j in range(s[i],f[i]):
        if j not in ans:
            meet=False
            #print(s[i],f[i])
            #print(ans)
            ans.extend(q)
            break
        else:
            for k in range(len(ans)):
                if ans[k]==j:
                    q.append(ans[k])
                    ans[k]="#"
    if meet:
        #print(s[i],f[i])
        mc+=1
print(mc)
