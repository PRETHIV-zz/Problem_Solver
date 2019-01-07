#prethiv
a,b,c=map(int,input().split(" "))
k=0
if a>=b and a>=c:
  print(a)
  k=1
elif b>=a and b>=c and k==0:
  print(b)
  k=1
elif c>=a and c>=b and k==0:
  print(c)
