#Swap_CHk
s=input()
lf=[]
cnt=0
ss=list(set(s))
for i in ss:
    g=0
    for j in s:
        if i==j:
            g+=1
    lf.append(g)
for i in lf:
    if i==1:
        cnt+=1
#print(lf)
#print(cnt)
#print(len(s)//2)
if cnt>=len(s)//2:
    print("yes")
else:
    print("no")
