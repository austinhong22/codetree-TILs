a_count = 0

for _ in range(3):
    symptom, temperature = input().split()
    temperature = float(temperature)

    if symptom == "Y" and temperature >= 37:
        a_count += 1

print("E" if a_count >= 2 else "N")