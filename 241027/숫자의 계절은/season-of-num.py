m = int(input())

if m <=2 or m == 12:
    print("Winter")
elif m == 3 or m <=5:
    print("Spring")
elif m == 6 or m <= 8:
    print("Summer")
else:
    print("Fall")