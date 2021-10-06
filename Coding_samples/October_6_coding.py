# in-class coding from Wednesday, October 6 2021

state_list = ["Washington","Oregon","California", "Arizona",
              "Nevada", "Idaho","Montana", "Wyoming", "Utah",
              "Colorado"]

word = "supercalifragilisticexpialidocius"

i = 0
reversed_list = []
while i < len(state_list):
    reversed_list.insert(0,state_list[i])
    print(reversed_list)
    input("Press enter to continue")
    i += 1

print(reversed_list)

i = len(state_list)-1
reversed_list = []
while i >= 0:
    reversed_list.append(state_list[i])
    print(reversed_list)
    input("Press enter to continue")
    i -= 1

print(reversed_list)

reversed_list = []
for state in state_list:
    reversed_list.insert(0, state)

print(reversed_list)

i = 0
reversed_word = []
while i < len(word):
    reversed_word.insert(0,word[i])
    i += 1

print(reversed_word)

joined_word = "".join(reversed_word)
print(joined_word)

wl =list(word)

i = 2
codeword = []
while i <= 20:
    codeword.append(word[i])
    i += 2

print(codeword )

#boolean flag while loops

x = int(input("Please enter a number"))
j = x > 3
while j:
    print("Good job")
    x = int(input("Pleaes enter a number"))
    j = x> 3

while x>3:
    ...

"""
header comment
"""