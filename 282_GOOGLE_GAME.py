#Input commands
s=input()
lt=['u','b','d','w']
rt=['u','w','d','b']
x=0
y=0
pos='u'
for i in s:
    if i=='G':
        if pos=='u':
            y+=1
        elif pos=='b':
            x-=1
        elif pos=='d':
            y-=1
        else:
            x+=1
    else:
        if i=='L':
            for i1 in range(4):
                if lt[i1]==pos:
                    pos=lt[(i1+1)%4]
                    break
        else:
            for i1 in range(4):
                if rt[i1]==pos:
                    pos=rt[(i1+1)%4]
                    break
if x==0 and y==0:
    print("yes")
else:
    print("no")
