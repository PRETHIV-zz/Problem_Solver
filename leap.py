def chkyr(y):
  if y%400==0:
    return True
  if y%100==0:
    return False
  if y%4==0:
    return True
  return False
n=int(input())
if chkyr(n):
  print("yes")
else:
  print("no")
