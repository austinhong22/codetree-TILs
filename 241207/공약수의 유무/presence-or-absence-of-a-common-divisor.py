from math import gcd

a, b = map(int,input().split())
satisfied = False
common_gcd = gcd(1920,2880)

for i in range(a,b+1):
    if i % common_gcdgcd == 0:
        satisfied = True

if satisfied == True:
    print(1)
else:
    print(0)
