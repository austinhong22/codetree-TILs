inq = input().split()
a = int(inq[0])
b = int(inq[1])

if a < b:
    print("1", end=" ")
else:
    print("0", end=" ")

if a == b:
    print("1")
else:
    print("0")