n = int(input())
satisfied = False

for i in range(1,n):
    if n % i == 0:
        satisfied = False
    else:
        satisfied = True

if satisfied == True:
    print("P")
else:
    print("C")