
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
        score = input("SCORE DUMMY ")

        if name =="":
            print("ITS NO USE HIDING GIVE ME THEIR NAME BUTTFRICK ")
        else:
            students.append(name)
        if score =="":
            print("SCORE THEM IDIOT OR ILL SKIN YOU ALIVE ")
        else:
            scores.append(score)
            break

print(students)
print(scores)