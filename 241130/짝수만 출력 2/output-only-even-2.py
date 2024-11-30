arr =input().split()
b = int(arr[0])
a = int(arr[1])

while b >=a :
    if b % 2 == 0:
        print(b,end=" ")
    b -= 1