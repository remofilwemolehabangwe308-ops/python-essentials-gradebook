# Student Gradebook Manager - Remofilwe Molehabangwe - Python Essentials 1

# Returns the average of a list of marks, or None if the list is empty
def calculate_average(marks):
  pass

# Returns the highest and the lowest mark as tuple:(highest, lowest)
def highest_and_lowest(marks):
    if not marks:
      print("No marks yet")
      return None, None


    highest = max(marks)
    lowest = min(marks)
    return highest, lowest

# Asks for a mark, validates it with try-except, returns the float or None
def read_valid_mark():
 pass

# Add a new student to the gradebook dictionary
def add_student(gradebook):
 student_name = input("Enter the student name: ")
 while True:
  if not student_name:
    print("It is blank the student was not added")
    return 
  elif student_name in gradebook:
    print(f'{student_name} already exists')
    return 
  else:
    print(f'{student_name} added successfully')
    gradebook[student_name] = []
    break 

# Add one validated mark to an existing student 
def add_mark(gradebook):
 student_name = input("Enter the student name: ")
 if student_name not in gradebook:
  print(f"{student_name} does not exist.")
  return 
 else:
  while True:
    try:
      student_mark = float(input("Enter the student mark: "))
      if student_mark < 0 or student_mark > 100:
        print("Out of range!!!")
        return
      elif student_mark >= 0 and student_mark <= 100:
        gradebook[student_name].append(student_mark)
        print(f'Mark {student_mark} added to {student_name}')
        return
    except ValueError:
      print("That is not a number!!")

# Prints every student with marks and average
def view_all(gradebook):
  if not gradebook:
    print("No student yet: ")
    return
  else:
   for student_name in gradebook.keys():
      if not gradebook[student_name]:
        print(f'Student Name:{student_name}\nMarks: No marks yet\nAverage: n/a')
      else:
        average_mark = sum(gradebook[student_name]) / len(gradebook[student_name])
        print(f'Student Name:{student_name}\nMarks:{gradebook[student_name]}\nAverage:{average_mark}')

# Prints one student's full summary
def student_summary(gradebook):
  student_name = input("Enter the student name: ")
  if student_name not in gradebook:
    print(f'{student_name} does not exist')
    return
  marks = gradebook[student_name]
  number_of_marks = len(marks)
  highest, lowest = highest_and_lowest(marks)
  if highest is None and lowest is None:
   return
  average_mark = sum(marks)/len(marks)
  print(f'Student Name: {student_name}\nNumber of marks: {number_of_marks}\nAverage: {average_mark}\nHighest: {highest}\nLowest: {lowest}')

# Prints class statistics including pass/fail lists
def class_statistics(gradebook):
  if not gradebook:
    print("No student yet")
    return
  class_number = len(gradebook)
  total_marks = 0
  total_mark_count = 0 
  passing_list = []
  failing_list = []
  top_student = ("")
  highest_average = 0

  for student_name in gradebook.keys():
    if not gradebook[student_name]:
      print(f'{student_name} has no marks yet')
      continue 
    average_mark = sum(gradebook[student_name])/len(gradebook[student_name])
    if average_mark > highest_average:
      highest_average = average_mark
      top_student = student_name
    total_marks += sum(gradebook[student_name])
    total_mark_count += len(gradebook[student_name])
    if average_mark >= 50:
      passing_list.append(student_name)
    else:
      failing_list.append(student_name)
        
  if total_mark_count == 0:
    print("No marks yet")
    return
  class_average = total_marks/total_mark_count
  print(f'Total number of student:{class_number}\nClass Average:{class_average}\nTop Student:{top_student}\nHighest Average:{highest_average}\nPassing List:{passing_list}\nFailing List:{failing_list}')

# Removes a student after y/n confirmation
def remove_student(gradebook):
  student_name = input("Enter the student name: ")
  if student_name not in gradebook:
    print(f'{student_name} not found')
    return
  else:
    confirmation = input(f'Are you sure you want to remove {student_name}? (y/n)')
    if confirmation == "y":
       del gradebook[student_name]
       print(f'{student_name} is removed')
    else:
       print(f'{student_name} is not removed')
# ---- main program ----


gradebook = {}
while True:
  # print the menu,read the choice,call the right function
  print("1.Add a student\n2.Add a mark\n3.View all student\n4.Student summary\n5.Class statistics\n6.Remove a student\n7.Exit")
  option = input("Enter option: ")
  if option == '7':
    print("Goodbye!!!")
    break
  elif option == '1':
    add_student(gradebook)
  elif option == '2':
    add_mark(gradebook)
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
    

  
        
  


      
  
  

   
        
  


      
  
  
