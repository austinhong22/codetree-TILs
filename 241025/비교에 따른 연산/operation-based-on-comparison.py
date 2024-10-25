inq = input().split()
a = int(inq[0])
b = int(inq[1])

if a>b:
    print(f"{a*b}")
else:
    print(f"{b%a}")