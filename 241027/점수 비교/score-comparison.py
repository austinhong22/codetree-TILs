arr1 = input().split()
arr2 = input().split()

math_a = int(arr1[0])
eng_a = int(arr1[1])
math_b = int(arr2[0])
eng_b = int(arr2[1])

if math_a > math_b and eng_a > eng_b:
    print(1)
else:
    print(0)