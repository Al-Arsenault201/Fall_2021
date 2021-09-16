# in-class coding from Wednesday, September 15

# floating point division
y = 4.0/1.3
print(y)

#integer division
z = 4/3
print("floating point", z)
x = 4//3
print("integer divide", x)

# integer division with floating point?
z = 4.0//3.0

# comparison operators
5.0 >= 4.8

#strings
"Joe" == "Joe"

name = input("what is the student's name?")
print(name=="Joe")

# this section is about conditionals

major = input("Please enter your major")
if major=="Physics" or major=="physics":
    print("Congratulations. You have excellent taste")
    print("this is another line", end="::::")
    print("and again", "\n"," and more")

print ("This is the end of our program")


# the two-option case
major = input("Please enter your major")
if major=="Physics" or major=="physics":
    print("Congratulations. You have excellent taste")
    print("this is another line", end="::::")
    print("and again", "\n"," and more")
else:
    print("Good, but maybe think about Hawking next time")

print ("This is the end of our program")


# if you are at least 18 but not 21 you can do some things
# if you're under 18 you're a minor
# if you're 21 or over you're an adult and can pretty much do what you want

age =  int(  input("What is your age in years? "))
if age >= 21:
    print("you are an adult and can drink, smoke, gamble or whatever")
elif (age >= 18) and (age < 21):
    print("You're not a minor but you're not fully an adult")
else:
    print("Sorry, you're not yet 21, so you can't do a lot of stuff")

    age = int(input("What is your age in years? "))
    if age >= 21:
        print("you are an adult and can drink, smoke, gamble or whatever")
    elif (age < 21) and (age == 18):
        print("Congrats; no longer a minor")
    elif (age < 21) and (age != 18) and (age == 19):
        print("This is really getting silly")
    elif age == 20:
        print("You're not a minor but you're not fully an adult")
    else:
        print("Sorry, you're not yet 21, so you can't do a lot of stuff")

x = 5
y = 7
if (x % 2 == 1) and (y%2==1):
    print("X and Y are both odd")
if (x%2 == 1) or (y%2== 1):
    print("At least one is odd")