# in class coding for Monday, September 27

# some lists we'll use
grade_list = [98, 92.5, 123, 199.8]
lizards = ["gecko", "iguana", "komodo dragon",
           "chameleon"]
grocery_list = ["Milk", "Eggs", "Cereal", "Coffee",
            "Apples", "Strawberries", "Broccoli",
           "Cucumber", "Tomatoes", "Green Onions"]
mixed_list = ["eggs", 12, "milk", 128.0]


states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


vowels = ['a','e','i','o','u','y']

for i in range(len(states)):
    statename = states[i]
    if statename[-1] in vowels:
        print(statename)

#for each loop
for statename in states:
    if statename[-1] in vowels:
        print(statename)

#print out every state that ends in 'a'
for i in range(len(states)):
    statename = states[i]
    if statename[-1] == 'a':
        print(statename)



for i in range(-1,-1*len(grocery_list)-1,-1):
    print(grocery_list[i])

#for i loop:
for i in range(0,len(grocery_list),1):
    print(grocery_list[i])

#for each loop
for item in grocery_list:
    print(item)

# range statement allows defaults
for i in range(0,len(grocery_list)):  #if you only have two values, the hop count is 1

for i in range(len(grocery_list)):  # if you only have one value, it's the stopping point

    #there is no way to default to starting at 0, giving and end and having a hop count of 2

for i in range(len(grocery_list),2): # won't work



#print all the even integers between x and y
for i in range(x,y+1,1):
    if i%2 == 0:
        print(i)

for i in range(x,y+1,2):
    print(i)


#input validation
# ask the user for an integer - how do we know whether the user typed an integer?

num = int(input("Please enter the number of classes you're taking this semester"))


digits = ['0','1','2','3','4','5','6','7','8','9']

num = input("Please enter the number of classes you're taking this semester")
is_int = True
for i in range(len(num)):
    if num[i] in digits:
        print("That's a digit")
    else:
        is_int = False
if is_int == True:
    num = int(num)
    print("You said you're taking", num, "classes")
else:
    print("I'm sorry, that's not an integer")


#handle negative integers
#check first character in string:
# if it's a digit OR if it's '-' this is valid

num = input("how many classes are you taking")
if num[0] =='-' or num[0] in digits:
        is_int = True
        for i in range(len(num)):
            if num[i] in digits or num[i] == '-':
                print("That's a digit")
            else:
                is_int = False
        if is_int == True:
            num = int(num)
            print("You said you're taking", num, "classes")
        else:
            print("I'm sorry, that's not an integer")
else:
    print("I'm sorry, that's not an integer")
