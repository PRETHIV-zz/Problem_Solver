#Str_Dif__by_K_Char
def pretdif(s1,s2):
    a1=""
    a2=""
    for i in sorted(s1):
        a1+=i
    for j in sorted(s2):
        a2+=j
    c=0
    c=c+abs(len(a1)-len(a2))
    for i in range(len(a1)):
        if a1[i]!=a2[i]:
            c+=1
    return c
s1,s2,k=map(str,input().split())
n=int(k)
n1=pretdif(s1,s2)
if n==n1:
    print("yes")
else:
    print("no")
