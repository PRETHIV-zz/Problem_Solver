#sort_In_Reverse
a=input()
b=list(set(a))
b.sort()
b.reverse()
ans=""
for i in b:
    ans+=i
print(ans)
