# in-class coding from Wednesday, September 22

new_empty_list = []

new_grade_list = [10,9,10,8,10,50]

new_student_list = ["Arsenault", "Alfred", 42, 54,"CSEE","COEIT", 353]

len(new_grade_list)

#the last element always has index len() -1
# we can abbreviate as -1
new_grade_list[-1]

if 42 in new_student_list:
  print("The answer to life, the universe and everything")
else:
  print("What do you mean it's missing?")

#adding to a list
#adding to the end with append
new_grade_list.append(50)

del new_grade_list[0:4]

# a list of all the states in the US

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

states.append("DC")
#deleting a list element by index

states.pop(7)

# what if I want the first 10 states?
first_ten = states[0:10]

num_states = len(states)
midpoint = num_states//2
start = midpoint - 5
end = midpoint + 5
mid_ten = states[start:end]

# if you don't give an initial value, the slice starts at the beginning of the list
# - with 0

first_ten = states[:10]

# if you don't put an end value, the slice stops at the end of the list

last_ten = states[40:]


# the whole list
all = states[:]


# strings

stringvar = "University of Maryland-Baltimore County"
len(stringvar)

newstring = stringvar[0:5]

#you can tell the position of every character in a string
stringvar[0]

#you can change the value of an element of a list
states[3] = "ARK"

#you cannot do that with a string
stringvar[10] = "-"

#splitting a string
s = input("Type a sentence here")

#create a list
l = s.split()  #default - splits on whitespace

#the character you split on is thrown away
# split on anything - split on anything
new_list = s.split('d')

#split always returns a list of strings

grades = input("Enter the user's grades with a blank space between each")

#split into grades
grade_list = grades.split()

#string stripping
sentence = input("Enter a sentence here")
left_justified = sentence.lstrip()
right_justified = sentence.rstrip()
clean = sentence.strip()



