cnt1 = 0
cnt2 = 0

for _ in range(10):
    a = int(input())
    if a % 3 == 0:
        cnt1 +=1
    if a % 5 == 0:
        cnt2 +=1
        
print(f"{cnt1} {cnt2}")