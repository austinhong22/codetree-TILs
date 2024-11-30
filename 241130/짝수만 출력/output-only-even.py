arr = input().split()
a = int(arr[0])
b = int(arr[1])
i = a
while a<=b:
    if a % 2 == 0:
        print(a, end=" ")
    a +=1