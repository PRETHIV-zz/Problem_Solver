#prethiv n l r min
n=int(input())
no=bin(n)
no=no[::-1]
for i in range(0,len(no)):
    if no[i]=='1':
        print(i+1)
        break
