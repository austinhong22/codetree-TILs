# 월을 입력받기
month = int(input())

# 월에 따른 일수를 출력
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:
    print(28)