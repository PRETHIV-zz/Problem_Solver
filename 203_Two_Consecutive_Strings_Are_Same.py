#prethiv n l r min
n=int(input())
c=0
a=[]
for i in range(n):
    s=input()
    a.append(s)
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        print("yes")
        c+=1
        break
if c==0:
    print("no")
