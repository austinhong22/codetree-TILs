arr = list(map(float, input().split()))
sum_val = 0
	
# 배열에 저장된 원소들의 합을 구합니다.
sum_val = sum(arr)

# 평균을 구하여 출력합니다.
print(f"{sum_val / 8:.1f}")