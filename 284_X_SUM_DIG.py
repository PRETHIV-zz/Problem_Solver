#nofind
nn=int(input())
ans=[1]
a2=[]
for i in range(nn,-1,-1):
    #print(xsumtot(str(i)),i)
    q=i+sum(list(map(int,str(i))))
    if nn==q:
        a2.append(i)
    if q<nn-2:
        break
a2.reverse()
ans.extend(a2)
for i in ans:
    print(i)
