satisfied = False

for i in range(5):
    a = int(input())
    if a % 3 == 0:
        satisfied = True
    else:
        satisfied = False

if satisfied == True:
    print(1)
else:
    print(0)