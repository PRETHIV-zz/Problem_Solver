#guvi I am prethiv
s=input()
abc=0
oc=0
for i in s:
    if i=="a" or i=="b":
        abc+=1
    else:
        oc+=1
if oc==0 or oc==1:
    print("yes")
else:
    print("no")
