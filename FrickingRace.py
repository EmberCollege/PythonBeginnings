times = []

for l in range(0,5):
    while True:
        try:
            raceTimes = input("Enter a race time in the format '10.12'")
            raceTimes = float(raceTimes)

            print("Lane", l, "has the time of", raceTimes)

            if raceTimes < 8 or raceTimes > 50:
                input("Please enter a valid race time")
            else:
                times.append(raceTimes)
            break
        except:
            raceTimes = input("Please enter a number in the format of '10.12'")
            break

print(times)