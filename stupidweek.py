while True:
    try:
        weekSpend = input("Enter your weekly spend, eg '150.65': ")
        weekSpend = float(weekSpend)

        if weekSpend < 0 or weekSpend > 1000:
            weekSpend = input("Sorry, that is too little or too much, please input a number between 0 and 1000: ")
        else:
            print("Thats all good!")
        break
    except:
        weekSpend = input("Enter a valid format!: ")
        break