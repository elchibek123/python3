# Python Dictionary

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Retrieving items from dictionary.
# print(programming_dictionary["Bug"]

# Adding new items to dictionary.   
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe and existiong dictionary.
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary.abs
for key  in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

  # Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    
print(student_grades)