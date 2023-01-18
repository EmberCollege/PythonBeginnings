students = []
scores = []

while True:
    try:
        noStudents = input("HOW MANY FRICKIN STUDENTS ARE IN YOUR BASEMENT ")
        noStudents = int(noStudents)
        break
    except:
        noStudents = input("EnTER a NUmBEr IdiOT ")
        break

for student in range(0,noStudents):
    while True:
        name = input("Name IDIOT ")

        if name =="":
            print("ITS NO USE HIDING GIVE ME THEIR NAME BUTTFRICK ")
        else:
            students.append(name)
            break
    while True:
        score = input("WHAT SCORE ENTER OR I SKIN YOU ALIVE ") # Asks to enter a score
        try:
            score = int(score)
        except:
            score = input("IM GETTING MY KNIFE TO SKIN YOU ALIVE")


print(students)