# 두 정수를 입력받기
a, b = map(int, input("두 정수를 입력하세요: ").split())

# a부터 b까지의 홀수를 출력
for i in range(a, b + 1):
    if i % 2 != 0:  # 홀수인지 확인
        print(i, end=" ")
