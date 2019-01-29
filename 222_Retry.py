#Ready to Hunt
n=int(input())
a=list(map(int,input().split()))
ln=[]
c=0
for i in range(1,len(a)+1):
    ln.append(i*n)
for i in range(len(a)):
    if a[i] in ln:
        c+=1
print(c)
