#Marana Hunter
import sys
name=""
c=True
mt=0
for line in sys.stdin:
    lt=list(map(str,line.split("#")))
    if c:
        c=False
        o=lt[1:]
        for i in o:
            mt+=int(i)
        name=lt[0]
    m=0
    o=lt[1:]
    for i in o:
        m+=int(i)
    if m>mt:
        name=lt[0]
        mt=m
print(name)
