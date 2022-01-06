#Question 1 
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))
sum=x+y+z
average=sum/3
print("The average of the three numbers is: {}".format(average))

#Question 2
gross_income = int(input("Enter your gross income: "))
number_of_dependents = int(input("Enter number of dependents: "))
taxable_income= gross_income-10000-3000*number_of_dependents
income_tax=taxable_income/5
net_income=taxable_income-income_tax
print("Your income tax is: {}".format(income_tax))
print("Your net income is: {}".format(net_income))

#Question 3
sid=int(input("Enter your SID: "))
name=str(input("Enter your name: "))
gender=str(input("Enter your gender (M/F/U): "))
course_name=str(input("Enter your course name: "))
cgpa=float(input("Enter your CGPA: "))
student=[sid, name, gender, course_name, cgpa]
print(student)

#Question 4
first_student=int(input("Enter the marks of first student: "))
second_student=int(input("Enter the marks of second student: "))
third_student=int(input("Enter marks of third student: "))
fourth_student=int(input("Enter marks of fourth student: "))
fifth_student=int(input("Enter marks of fifth student: "))
list_of_marks=[first_student, second_student, third_student, fourth_student, fifth_student]
list_of_marks.sort()
print(list_of_marks)

#Question 5a
color=["Red", "Green", "White", "Black", "Pink", "Yellow"]
print(color)
color.pop(3)
print(color)

#Question 5b
color=["Red", "Green", "White", "Black", "Pink", "Yellow"]
color[3:5]=["purple"]
print(color)


