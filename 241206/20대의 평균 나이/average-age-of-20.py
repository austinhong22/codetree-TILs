ages = []
while(True):
    age =int(input())

    if age >=30 or age <20:
        break
    ages.append(age)


avg = sum(ages)/len(ages)
print(f"{avg:.2f}")
        