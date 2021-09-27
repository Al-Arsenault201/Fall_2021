# in class coding from Monday, September 13

#basic print statement

print("hello, world") # print a literal value

#single quotes are fine
print('hello, world')

x = 5
print(x) # print a variable

# printing multiple lines of output

#use multiple print statements
print("This is CMSC 201")
print("Section 60")
print("We meet on Monday and Wednesday")

print("This is CMSC 201", end=' ')
print("Section 60", end=' ')
print("We meet on Monday and Wednesday")

#a single print statement
print("This is CMSC 201", "Section 60", "We meet on Monday and Wednesday")


print("This is CMSC 201"+"Section 60"+ "We meet on Monday and Wednesday")

#mixing types
print("The answer is:", 42)

#printing newlines
print("This is CMSC 201", "\n", "Section 60", "\n", "We meet on Monday and Wednesday")

#ask the user for her GPA last semester
gpa = input("Please enter your GPA from last semester") # yields a string
actual_gpa=float(gpa)  #converts the string to a floating point number

points = actual_gpa * 15 #presumes you took 15 semester hours
print ("You had ", points, "Points")

movie = input("What is your favorite movie?")
why = input("why do you like"+movie)


#operators - assignment
a = 42  # assigns the value of 42 to location in memory represented by a

#comparison - always returns a Boolean value - True or False
a == 42

# more assignments
a += 1 #same as a = a + 1
a-= 1
a*= 5
a /= 5

