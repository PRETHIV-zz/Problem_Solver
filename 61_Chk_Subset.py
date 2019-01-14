#guvi this is roky
n,m=map(int,input().split())
l=list(map(int,input().split()))
l2=list(map(int,input().split()))
flag=0
if len(l2)>len(l):
    print("NO")
    flag=1
else:
    for i in range(len(l2)):
        for j in range(len(l)):
            if l2[i]==l[j]:
                l[j]="#"
                l2[i]="#"
    for i in l2:
        if i!="#":
            print("NO")
            flag=1
            break
    if flag==0:
        print("YES")
