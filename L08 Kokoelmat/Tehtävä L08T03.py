#Lab08 Tehtävä 03

# create the list
course_grades = []

# ask for course grades and add each one to the list. An empty entry stops the loop.
while True:
    grade = input("Anna arvosana: ")
    if grade == "":
        break
    elif int(grade) >= 0 and int(grade) <= 5:
        course_grades.append(int(grade))

# calculate the average grade
average = sum(course_grades)/len(course_grades)

# print the number of ratings and the average grade
print(f"Annoit {len(course_grades)} arvosanaa")
print(f"Arvosanojen keskiarvo on {average:.1f}")