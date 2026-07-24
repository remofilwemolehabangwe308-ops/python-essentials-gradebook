# Student Gradebook Manager - Remofilwe Molehabangwe - Python Essentials 1
# Returns the average of a list of marks, or None if the list is empty
def calculate_average(marks):
# Returns the highest and the lowest mark as tuple:(highest,lowest)
def highest_and_lowest(marks):
# Asks for a mark, validates it with try-except, returns the float or None
def read_valid_mark():
# Adds a new student to the gradebook dictionary 
def add_student(gradebook):
# Adds one validated mark to an existing student
def add_marks(gradebook):
# Prints every student with marks and average
def view_all(gradebook):
# Prints one students's full summary
def student_summary(gradebook):
# Prints class statistics including pass/fail lists
def class_statictics(gradebook):
# Removes a student after y/n confirmation
def remove_student(gradebook):
# ---- main program ----
gradebook = {}
while True:
  # print the menu,read the choice,call the right function
