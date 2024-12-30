n = int(input())

for i in range(1, n + 1):
    # 현재 줄에 출력할 '*'의 개수를 계산합니다.
    star_count = 2 * i - 1
    
    # '*'을 star_count 개수만큼 반복하여 출력합니다.
    for j in range(star_count):
        print("*", end="")
    
    # 현재 줄의 별 출력이 끝났으므로 줄 바꿈을 합니다.
    print()