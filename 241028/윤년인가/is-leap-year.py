y = int(input())

if y % 4 == 0 or (y % 400 == 0 and y % 100 == 0 ):
    print("true")
else:
    print("false")