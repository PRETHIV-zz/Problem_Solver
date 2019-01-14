# Hello World program in Python
    
#hi guvi i am rocky from home towny
n=int(input())
s=input()
l=[]
for i in s:
    try:
        l.append(int(i))
    except:
        continue
ans=[]
for i in range(len(l)):
    if i%2==0 and l[i]%2==1:
        ans.append(l[i])
    elif i%2==1 and l[i]%2==0:
        ans.append(l[i])
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end=" ") 
        #hey manual reviewer here also i am using end=" " coz one case failed showing msg like expected op:1 2 1 ur op:1 2 1 but i used end="" at that time so only i changed
    else:
        print(ans[i],end=" ")
