#prethiv n l r min
def pretretlen(a,i,m):
    l=i+1
   # print(i,l,m)
    if l==m:
     #   print("end")
        return 1
    else:
        if a[i]==a[l]:
          #  print("bS")
            return 1+pretretlen(a,i+1,m)
        elif a[i]!=a[l]:
          #  print("NE")
            return 1
n,k=map(int,input().split())
c=0
a=[]
ans=[]
for i in range(n):
    s=input()
    a.append(s)
mm=len(a)
for i in range(len(a)):
    ans.append(pretretlen(a,i,mm))
 #   print("vvv")
if k in ans:
    print("yes")
else:
    print("no")
