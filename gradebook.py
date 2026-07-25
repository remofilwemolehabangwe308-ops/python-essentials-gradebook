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
  print("1.Add a student\n2.Add a mark\n3.View all student\n4.Student summary\n5.Class statistics\n6.Remove a student\n7.Exit")
  option = input("Enter option: ")
  if option == '7':
    break
  elif option == '1':
    add_student(gradebook)
  elif option == '2':
    add_marks(gradebook)
  elif option == '3':
    view_all(gradebook)
  elif option == '4':
    student_summary(gradebook)
  elif option == '5':
    class_statistics(gradebook)
  elif option == '6':
    remove_student(gradebook)
  else:
    print("Invalid option")
    
def add_student(gradebook):
  student_name = input("Enter the student name: ")
  while True:
    if not student_name:
      print("It is blank the student was not added")
      return Menu
    elif student_name in gradebook:
      print(f'{student_name} already exists')
      return Menu
    else:
      print(f'{student_name} added successfully')
      gradebook[student_name] = []
      break 
      
  
  
