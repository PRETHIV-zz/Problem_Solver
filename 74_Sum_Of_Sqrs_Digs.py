#Include sum_of_sqrs_of_digs
n=input()
c=0
for i in n:
  if i.isnumeric():
    c+=int(i)*int(i)
print(c)
