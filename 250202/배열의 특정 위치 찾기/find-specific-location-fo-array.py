arr = list(map(int, input().split()))
filtered_arr = arr[::2]

sum_val = sum(filtered_arr)
print(sum_val)