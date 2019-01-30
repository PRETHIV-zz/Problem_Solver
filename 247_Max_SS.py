#Sum_Of_Subarray
n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(len(a)):
    s=a[i:]
    ans.append(sum(s))
for i in range(len(a)-1,-1,-1):
    s=a[i::-1]
    ans.append(sum(s))
print(max(ans))
