n=input()
try:
    f=float(n)
    print("yes")
except:
    try:
        i=int(n)
        print("yes")
    except:
        print("No")