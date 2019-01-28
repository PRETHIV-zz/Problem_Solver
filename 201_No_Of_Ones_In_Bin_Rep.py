#prethiv n l r min
n=int(input())
on=bin(n)
on=on[2:]
c=0
for i in on:
    if i=="1":
        c+=1
print(c)
