#in-class coding from Wednesday, September 29

#while loops - used for controlling user input

num = int(input("Enter a number between 0 and 9 inclusive"))  #priming read

#what if the user entered -5?
while num < 0 or num > 9:
    print("That was not a valid entry")
    num = int(input("Enter a number between 0 and 9 inclusive"))

age = 0
while (age < 18):
    age = int(input("enter your age in years: "))
    print ("If you’re 18 or older you should vote")
print ("that’s the end of our story")


#factorial
product = 1
fact = int(input("What number shall we compute the factorial of"))
while fact>=1:
    product = fact * product
    fact -= 1
print(fact, " factorial is ", product)

#factorial as a for loop
product = 1
fact = int(input("What number shall we compute the factorial of"))
for i in range(1,fact+1):
    product *= i
#    print(product)
print(fact, " factorial is ", product)

#print the even integers between 2 and a number
num = int(input("enter an integer"))
while num%2 == 0 and num < 100:
    print(num)
    num += 2

#infinite loop - never stops
#print the even integers from 0 to 100
num = int(input('enter an integer'))
while num != 100:
    print(num)
    num += 2


grade = ""
name  = ""
while name != "Hrabowski":
    # get the user's grade
    grade = input("What is your grade? ")
print("You passed!")


cookiesLeft = 50

while cookiesLeft > 0:
    # eat a cookie
    cookiesLeft = cookiesLeft + 1


#enter the classes you're taking
c = input("Enter the first class you're taking. Enter q or Q to quit")
class_list = []
while c != 'q' and c != 'Q':
    class_list.append(c)
    c = input("Enter the next class you're taking. Enter q or Q to quit")
print(class_list)


#boolean flag
prompt = "Tell me something cool: "
prompt += "\nEnter 'quit' to end the program"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
       active = False
    else:
       print(message)


