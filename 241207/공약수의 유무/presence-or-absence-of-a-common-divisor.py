a, b = map(int, input().split())

found = 0
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:  # i가 두 수 모두를 나누어떨어뜨리는지 검사
        found = 1
        break

print(found)
