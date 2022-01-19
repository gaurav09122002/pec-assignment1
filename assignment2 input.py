#QUESTION 1 
string="Python is a case sensitive language"
length=len(string)
print("a.  length of the input string is ",length)
x=string[::-1]
print("b.  reverse order of the input string  --> ",x)
x=string[10:26]
print("c.  New string =",x)
x=string.replace("a case sensitive" , "object oriented")
print("d. ",x)
x=string.find("a")
print("e.  index of substring a in input string  --> ",x)
x=string.replace(" " , "")
print("f. ",x)

print("\n\n")

#QUESTION 2
_name=str(input("enter your name: "))
_SID=int(input("enter your SID: "))
_branch=str(input("enter your department: "))
_CGPA=float(input("enter your CGPA: "))
print("Hey, ",_name," here!")
print("My SID is ",_SID,)
print("I am from ",_branch," department and my CGPA is ",_CGPA)

print("\n\n")

#QUESTION 3
a=56
b=10
print("a.  a&b  -->  ",a&b)
print("b.  a|b  -->  ",a|b)
print("c.  a^b  -->  ",a^b)
print("d. left shift a with 2 bits (a<<2)  -->  ",a<<2)
print("   left shift b with 2 bits (b<<2)  -->  ",b<<2)
print("e. right shift a with 2 bits (a>>2)  -->  ",a>>2)
print("   right shift b with 4 bits (b>>4)  -->  ",b>>4)

print("\n\n")

#QUESTION 4
x=input("enter first number: ")
y=input("enter second number: ")
z=input("enter third number: ")
if x>=y and x>z:
    print(x)
elif x<y:
    if y>z:
        print(y)
    else:
        print(z)

print("\n\n")

#QUESTION 5
string=str(input("enter a string: "))
if 'name' in string:
    print("yes")
else:
    print("no")

print("\n\n")

#QUESTION 6
x=int(input("enter the first side: "))
y=int(input("enter the second side: "))
z=int(input("enter the third side: "))
if (y+z>=x and x+z>=y and x+y>=z):
    print("yes")
else:
    print("no")



 
