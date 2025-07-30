#!/usr/bin/env python
# coding: utf-8

# In[37]:


# Setup
# Install Python:

# Visit: https://www.python.org/downloads/

# Install the latest version (recommend 3.10 or later).

# Install Anaconda (Recommended):

# Visit: https://www.anaconda.com/products/distribution

# Download and install for your OS.

# Verify installation:

# Open Anaconda Navigator or launch Jupyter Notebook.

# In terminal or Anaconda prompt, run: python --version


# In[1]:


# Part 2: Basic Python Programming
#A. Write a Python program to check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# In[2]:


#B. Use a loop to print the first 10 natural numbers
for i in range(1, 11):
    print(i)


# In[3]:


# C. Write a function that returns the factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Factorial of 5 is:", factorial(5))


# In[4]:


#D. Create a function that checks if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


# In[5]:


#E. Use a while loop to sum numbers until the total exceeds 100
total = 0
i = 1

while total <= 100:
    total += i
    i += 1

print("Sum exceeded 100 with total:", total)


# In[6]:


# Lab Assignment: Working with Lists, Dictionaries, and File Handling


# In[7]:


# Part 1: List Operations
#A. Create a list of 5 numbers. Print the square of each number.
numbers = [2, 4, 6, 8, 10]
squares = [num ** 2 for num in numbers]
print("Squares:", squares)


# In[8]:


#B. Add a new number to the list and sort it in ascending order
numbers.append(3)
numbers.sort()
print("Sorted list:", numbers)


# In[9]:


#C. Remove the largest number from the list
numbers.remove(max(numbers))
print("List after removing max:", numbers)


# In[10]:


# Part 2: Dictionary Operations
# A. Create a dictionary with student names as keys and marks as values
marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(marks)


# In[11]:


#B. Add a new student and update marks for an existing student
marks["Diana"] = 88
marks["Alice"] = 90
print("Updated marks:", marks)


# In[12]:


#C. Print all students who scored above 80
for name, score in marks.items():
    if score > 80:
        print(f"{name} scored {score}")


# In[13]:


# Part 3: File Handling
# A. Write the student marks dictionary to a file called student_marks.txt
with open("student_marks.txt", "w") as f:
    for name, score in marks.items():
        f.write(f"{name}: {score}\n")


# In[15]:


# B. Read the contents of student_marks.txt and print them
with open("student_marks.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)


# In[16]:


#C. Read the file line by line and create a new dictionary from it
new_marks = {}
with open("student_marks.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(": ")
        new_marks[name] = int(score)

print("Reconstructed dictionary:", new_marks)


# In[17]:


'''Write a program that:

Accepts 5 student names and scores from user input

Stores them in a dictionary

Writes the dictionary to a file

Then reads the file back and prints the top 3 students'''


# In[18]:


# JSON Read/Write
# A. Create a dictionary and write it to a JSON file
import json

employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "HR",
    "skills": ["communication", "management"]
}

with open("employee.json", "w") as f:
    json.dump(employee_data, f, indent=4)

print("Employee data written to employee.json")


# In[19]:


# B. Read the JSON file and print the contents
with open("employee.json", "r") as f:
    data = json.load(f)

print("Employee Data:", data)
print("Name:", data["name"])
print("Skills:", ", ".join(data["skills"]))


# In[20]:


#C. Update the data (add a new skill) and save it back
data["skills"].append("teamwork")

with open("employee.json", "w") as f:
    json.dump(data, f, indent=4)

print("Updated employee data with new skill saved.")


# In[21]:


# Exception Handling
# A. Handle division by zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")


# In[22]:


#B. Handle invalid input types
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: That's not a valid integer.")


# In[23]:


# C. Handle file not found error
try:
    with open("non_existing_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")


# In[24]:


# D. Using finally block
try:
    f = open("sample.txt", "w")
    f.write("This is a test.")
    print("File written.")
except IOError:
    print("Error: Could not write to file.")
finally:
    f.close()
    print("File closed.")


# In[25]:


'''Create a program that:

Accepts user info: name, age, and a list of skills.

Writes this to a JSON file.

Then attempts to read the file back and:

If successful, prints the data.

If the file is missing, shows an error and exits safely.'''


# In[26]:


###Lab Assignment: CSV, Pandas & Object-Oriented Programming (OOP)


# In[27]:


# Part 1: CSV Reading and Writing
# A. Write a list of student dictionaries to a CSV file
import csv

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 76},
    {"name": "Charlie", "score": 93}
]

with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)

print("CSV file written.")


# In[28]:


#B. Read the CSV file and print student names and scores
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} scored {row['score']}")


# In[29]:


# Part 2: Basic Data Analysis with Pandas
# A. Read students.csv with pandas and display summary
import pandas as pd

df = pd.read_csv("students.csv")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())


# In[30]:


#B. Add a column for Pass/Fail based on score >= 80
df["Result"] = df["score"].apply(lambda x: "Pass" if x >= 80 else "Fail")
print(df)


# In[31]:


# C. Save updated DataFrame to a new CSV
df.to_csv("students_with_results.csv", index=False)
print("Updated CSV saved.")


# In[32]:


# Part 3: Object-Oriented Programming (OOP)
# A. Create a Student class with attributes and method
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def has_passed(self):
        return self.score >= 80

# Example usage
s1 = Student("Alice", 88)
print(f"{s1.name} passed: {s1.has_passed()}")


# In[33]:


#B. Create a list of Student objects and display results
students_list = [
    Student("Bob", 76),
    Student("Charlie", 93),
    Student("Diana", 81)
]

for student in students_list:
    print(f"{student.name}: {'Pass' if student.has_passed() else 'Fail'}")


# In[36]:


#C. Extend the class to include a method to convert to dictionary
# Updated Student class with to_dict() method
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def has_passed(self):
        return self.score >= 80

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score,
            "result": "Pass" if self.has_passed() else "Fail"
        }

# Create the students list AFTER defining the full class
students_list = [
    Student("Alice", 85),
    Student("Bob", 72),
    Student("Charlie", 90),
    Student("Diana", 65)
]

# Convert all student objects to dicts and save as CSV
import pandas as pd
student_dicts = [s.to_dict() for s in students_list]
df_students = pd.DataFrame(student_dicts)
df_students.to_csv("students_class_output.csv", index=False)


# In[35]:


'''Build a class called Course that:

Takes a course name and a list of Student objects

Can calculate the class average

Can print a list of passed and failed students'''


# In[ ]:




