N = int(input())

result = []
for _ in range(N):
    num = int(input())
    if num % 2 != 0 and num % 3 == 0: 
        result.append(num)

for num in result:
    print(num)