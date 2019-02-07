#nofind
nn=int(input())
a2=[]
for i in range(nn,-1,-1):
    #print(xsumtot(str(i)),i)
    q=i+sum(list(map(int,str(i))))
    if nn==q:
        a2.append(i)
    if q<nn-2:
        break
a2.reverse()
print(len(a2))
for i in a2:
    print(i)
