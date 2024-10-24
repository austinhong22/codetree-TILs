inq = input().split()
a = int(inq[0])
b = int(inq[1])

c = (10000*b)//(a*a)

if c>25:
    print(f"{c}\nObesity")
else:
    print(c)