# in-class coding for Monday, September 20

# first an examplesimulator
# to illustrate the use of conditionals in Python programs

#ask the user for her birthdate and birth month
birthdate =   int(input("Please enter the date of the month on  which you were born"))
birthmonth = int(input("Please enter the number of the month in which you were born"))

if (birthdate == 1) and (birthmonth == 1):
    print("Congratulations New Years baby")
else:
    print('not quite')


#another way to write the same code using nested if statements
if (birthdate==1):
    if (birthmonth==1):
        print("Congratulations New Years baby")
else:
    print("whatever ")



grocery_list = ["Milk", "Eggs", "Cereal", "Coffee",
  "Apples", "Strawberries", "Broccoli", "Cucumber",
  "Tomatoes", "Green Onions"]


g_list =[]
g_list.append("Milk")
g_list.append("Eggs")  #append always adds one value to the end of the list

#the remove method only removes the first occurrence of the value from the list
grocery_list.remove("Milk")

#what if the value is not there?
grocery_list.remove("UMBC")

#in
if "UMBC" in grocery_list:
    grocery_list.remove("UMBC") #prevents program from crashing

#always start counting from 0
#access one element of a list
grocery_list[1]

#len - tells you how many elements are in the list
# the first element is always [0]
# the last element is always [len - 1]

#insert
grocery_list.insert(3, "Half and Half")

#shortcut - the last element is always [len() - 1]
#you can abbreviate that as -1
grocery_list[-1]
