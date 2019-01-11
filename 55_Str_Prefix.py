# Hello World program in Python
#guvi this is rocky
n=int(input())
a=[]
for i in range(n):
    a.append(input())
ans=a[0]
for i in a:
    a1=""
    for j in range(len(ans)):
        if i[j]!=ans[j]:
            ans=a1
            break
        else:
            a1+=ans[j]
print(ans)
