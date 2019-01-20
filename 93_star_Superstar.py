#Star_Superstar
n=int(input())
a=list(map(int,input().split()))
st=[]
#st finding
for i in range(len(a)):
    c=0
    ref=len(a)-i-1
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            c+=1
    if c==ref:
        st.append(a[i])
#Spst_Finding
m=max(a)
for i in range(len(st)):
    if i==len(st)-1:
        print(st[i],end="")
    else:
        print(st[i],end=" ")
print()
print(m)
