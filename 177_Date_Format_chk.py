#DD_Format_Founder
s=input()
lt=list(map(str,s.split("/")))
c=0
try:
    for i in lt:
        if len(i)==2 and c==0:
            if i.isnumeric() and int(i)>=0 and int(i)<=31:
                c+=1
        elif len(i)==2 and c==1:
            if i.isnumeric() and int(i)>=0 and int(i)<=12:
                c+=1
        elif len(i)==4 and c==2:
            if i.isnumeric():
                c+=1
    if c==3:
        print("yes")
    else:
        print("no")
except:
    print("no")
