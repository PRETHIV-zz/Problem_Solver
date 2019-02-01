#Python hater
money=int(input())
c=0
while money!=0:
    if money>=1000:
        money-=1000
        c+=1
    elif money in range(500,1000):
        money-=500
        c+=1
    elif money in range(100,500):
        money-=100
        c+=1
    elif money in range(50,100):
        money-=50
        c+=1
    elif money in range(10,100):
        money-=10
        c+=1
    else:
        money-=1
        c+=1
print(c)
