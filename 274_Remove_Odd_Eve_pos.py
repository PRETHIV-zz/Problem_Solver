#remove odd eve pos
ans=[]
def findans(v):
    m=len(v)
    if m==0:
        return
    else:
        l=len(v)
        if l%2==0:
            mid=l//2
            tot=v[mid]+v[mid-1]
            avg=tot//2
            ans.append(avg)
            del v[mid]
            del v[mid-1]
        else:
            mid=l//2
            ans.append(v[mid])
            del v[mid]
        findans(v)
n=int(input())
a=list(map(int,input().split()))
findans(a)
for i in ans:
    print(i)
