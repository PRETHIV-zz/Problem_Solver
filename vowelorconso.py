l=['a','e','i','o','u','A','E','I','O','U']
c=input()
k=0
if c in l:
  print("Vowel")
elif not c.isAlpha():
  print("invalid")
else:
  print("Consonant")
