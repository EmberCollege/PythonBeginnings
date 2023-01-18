days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
price = []
totalPrice = 0

for d in range(0,5):
    while True:
        try:
            lunchPrice = input("Enter your lunch price in the format '10.12'")
            lunchPrice = float(lunchPrice)

            print("On", days[d],"you spent", lunchPrice)
            totalPrice += lunchPrice
            avgPrice = totalPrice/5
            price.append(lunchPrice)

            break
        except:
            lunchPrice = input("Please enter a number in the format of '10.12'")
            break

print("During the week, you spent", round(totalPrice,2))
print("On average, you spent", round(avgPrice,2))