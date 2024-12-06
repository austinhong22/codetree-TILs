n = int(input())

cnt = 1

for i in range(1,n+1):
    a = n//i
    if a > 1:
        cnt += 1
        n = a
        continue
    else:
        break
print(cnt)