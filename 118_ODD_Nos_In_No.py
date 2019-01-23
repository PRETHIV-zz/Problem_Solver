#prethiv.n
n=input()
l=[]
for i in n:
    if int(i)%2==1:
        l.append(int(i))
for i in range(len(l)):
    if i==len(l)-1:
        print(l[i],end="")
    else:
        print(l[i],end=" ")
