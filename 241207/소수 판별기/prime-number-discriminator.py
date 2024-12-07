n = int(input())
satisfied = False

for i in range(2,n):
    if n % i == 0:
        satisfied = False
        break
    else:
        satisfied = True

if satisfied == True:
    print("P")
elif satisfied == False:
    print("C")