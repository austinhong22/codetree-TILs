arr1 = input().split()
arr2 = input().split()

a_age = int(arr1[0])
a_sex = arr1[1]
b_age = int(arr2[0])
b_sex = arr2[1]

if (a_age >= 19 and a_sex == "M") or (b_age >= 19 and b_sex =="M"):
    print(1)