s1=input()
l=s1.split(" ")
ans=""
for i in range(len(l)):
    if i==len(l)-1:
        ans=ans+l[i][0].upper()+l[i][1:]
    else:
        ans=ans+l[i][0].upper()+l[i][1:]+" "
print(ans)
