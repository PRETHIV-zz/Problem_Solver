#prethiv n l r min
s=input()
abc=0
oc=0
for i in s:
    if i.isalpha() and i=="a" or i=="b":
        abc+=1
    else:
        oc+=1
        break
if oc==0:
    print("yes")
else:
    print("no")
