#max_Length_Of_Strings
s=input()
lts=list(map(str,s.split()))
ltl=[]
for i in lts:
    ltl.append(len(i))
m=max(ltl)
for i in range(len(ltl)):
    if ltl[i]==m:
        print(lts[i])
        break
