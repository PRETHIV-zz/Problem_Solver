s1,s2=map(str,input().split(" "))
l1=list(s1)
l2=list(s2)
c=0
l1.sort()
l2.sort()
if len(s1)!=len(s2):
    print("no")
else:
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            c=c+1
if c==1:
    print("yes")
else:
    print("no")
