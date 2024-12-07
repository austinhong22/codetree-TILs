from math import gcd

# 입력 받기
a, b = map(int, input().split())

# 1920과 2880의 최대공약수 계산
common_gcd = gcd(1920, 2880)

# 공약수 검사
found = 0
for i in range(a, b+1):
    if i % common_gcd == 0:
        found = 1
        break

# 결과 출력
print(found)