noStudents = input("Enter how many students there are")
studentArray = []

while True:
    try:
        noStudents = int(noStudents)

        for s in range(noStudents):
            name = input("What is their name?")
            score = input("What did they score?")
            studentArray.append(name,score)
        break
    except:
        noStudents = input("Please enter a number!")
        break

    
