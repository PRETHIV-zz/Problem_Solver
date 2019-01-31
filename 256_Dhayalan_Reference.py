def retlen(s,i):
    l=i+1
    if l==len(s):
        return 1
    else:
        if s[i]==s[l]:
            return 1+retlen(s,l)
        else:
            return 1
n=input()
f=[]
for i in range(len(n)):
    f.append(retlen(n,i))
#print(f)
ii=[0]
c=n[0]
for i in range(len(n)):
    if c!=n[i]:
        c=n[i]
        ii.append(i)
#print(ii)
for i in range(len(ii)):
    if i==len(ii)-1:
        print("("+str(f[ii[i]])+","+str(n[ii[i]])+")")
    else:
        print("("+str(f[ii[i]])+","+str(n[ii[i]])+")",end=",")
