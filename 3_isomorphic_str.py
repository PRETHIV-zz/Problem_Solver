s1=input()
s2=input()
ss1=set(s1)
ss2=set(s2)
if len(s1)!=len(s2):
    print("no")
else:
    if len(ss1)==len(ss2):
        print("yes")
    else:
        print("no")
