fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
    print(fruits)

# Find average height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

number_of_students = 0
for student in student_heights:
    number_of_students += 1

average_height = round(total_height / number_of_students)
print(average_height)

# Find highest score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}.")