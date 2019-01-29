#Ready to Hunt
def ispalin(s):
    ss=s[::-1]
    if s==ss:
        return True
    else:
        return False
s=input()
ss=[int(i) for i in s]
sumi=sum(ss)
if ispalin(str(sumi)):
    print("YES")
else:
    print("NO")
