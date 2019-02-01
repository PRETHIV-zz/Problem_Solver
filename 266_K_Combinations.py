#print_Check
n,k,t=map(int,input().split())
a=list(map(int,input().split()))
q=[]
find=False
for i in a:
    q.append([i])
#print(q)
if k==1:
    if t in a:
        print("YES")
    else:
        print("NO")
else:
    e3=[]
    for i in range(k-1):
        e=[]
        for j in range(len(a)):
            t1=[]
            for i1 in q:
                t1.append(i1)
            #print(t1)
            for k in range(len(q)):
                tt=q[k].copy()
                tt.append(a[j])
                #print(tt)
                e.append(tt)
                #print(e)
            #print("************")
            #print(e)
            q=[]
            #print(t1)
            for i2 in t1:
                q.append(i2)
            #print(q)
        e3=e.copy()
        #print("PPP",e3)
        q=e.copy()
    for i in e3:
        s=0
        for j in i:
            s+=j
        if s==t:
            find=True
            break
    if find:
        print("YES")
    else:
        print("NO")
#print(q)
