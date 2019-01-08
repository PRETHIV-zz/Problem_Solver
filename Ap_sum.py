#this is my own code guvi
n,a,d=map(int,input().split(" "))
l=[]
def ap_n(n,a,d):
    return (a+(n-1)*d)
for i in range(1,n+1):
    l.append(ap_n(i,a,d))
print(sum(l),end="")
