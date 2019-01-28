#ALternating character of vowels and consonants
s=input()
v=['a','e','i','o','u','A','E','I','O','U']
ans=[]
for i in range(len(s)):
    c=0
    for j in range(i,len(s)-1):
        if s[j] in v and not s[j+1] in v:
            c+=1
            if j+1==len(s)-1:
                c+=1
        if not s[j] in v and s[j+1] in v:
            c+=1
            if j+1==len(s)-1:
                c+=1
    ans.append(c)
print(max(ans))
