#guvi this is me
n=int(input())
l=list(map(int,input().split(" ")))
a1=" "
a2=" "
mi=" "
mi=str(l[0]+l[1])
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]<=int(mi) and l[i]+l[j]>=0:
            a1=str(l[i])
            a2=str(l[j])
            mi=str(l[i]+l[j])
print(a1,a2)
