#Ready to Hunt
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
s=input()
aa=[]
ss=""
for i in s:
    if i.isalpha():
        ss+=" "
        aa.append(i)
    else:
        ss+=i
na=list(map(int,ss.split()))
a=""
for i in range(len(aa)):
    if iseven(na[i]):
        a=a+(aa[i]*na[i])
    else:
        a=a+aa[i]+str(na[i])
print(a)
