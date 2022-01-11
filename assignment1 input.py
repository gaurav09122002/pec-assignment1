# QUESTION 1
print("enter first number: ")
num1 = int(input())
print("enter second number: ")
num2 = int(input())
print("enter thirdnumber: ")
num3 = int(input())
avg= (num1+num2+num3)/3
print("the average of three numbers: \n", avg)

print("\n\n")

#QUESTION 2
print("enter your gross income: ")
gross_income= int(input())
print("enter your dependants: ")
dependants= int(input())
taxable_income= gross_income-10000-(3000*dependants)
print("Your taxable income will be: \n", taxable_income)
print("your tax is: ", taxable_income*20/100, "\t(taxable income: ", taxable_income, ")")

print("\n\n")

#QUESTION 3
print("enter your name: ")
_name= input()
print("enter your SID: ")
_SID= input()
print("enter your gender: (Male:M , Female:F , Unknown:U)")
_gender= input()
print("enter course name (use the specific abbrevation)")
_course_name=input()
print("enter your CGPA: ")
_CGPA= float(input())
YOUR_IDENTITY_CARD= [_SID, _name, _gender, _course_name, _CGPA]
print("YOUR_IDENTITY_CARD\t---->\t", YOUR_IDENTITY_CARD)

print("\n\n")

#QUESTION 4
print("enter marks of student1: ")
marks1= float(input())
print("enter marks of student2: ")
marks2= float(input())
print("enter marks of student3: ")
marks= float(input())
print("enter marks of student4: ")
marks4= float(input())
print("enter marks of student5: ")
marks5= float(input())
students_marks= {"Student1":marks1, "Student2":marks2, "Student3":marks3, "Student4":marks4, "Student5":marks5]
print("List of students marks\t---->\t", students_marks)

print("\n\n")

#QUESTION 5
List_of_colours= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List_of_colours.remove('Black')
print(List_of_colours)
List_of_colours[3]= 'Purple'
print(List_of_colours)