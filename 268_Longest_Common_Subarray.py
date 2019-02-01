#Longest common subarray
s1=input()
s2=input()
maxi=0
ans=""
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            m=0
            ii=i
            jj=j
            while s1[ii]==s2[jj]:
                m+=1
                ii+=1
                jj+=1
                if len(s1)==ii or len(s2)==jj:
                    break
            if m>maxi:
                maxi=m
                ans=s1[i:i+maxi]
print(ans)
