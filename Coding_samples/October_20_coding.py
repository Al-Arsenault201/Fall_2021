# in-class coding for Wednesday, October 20

# introduction to functions

"""
here is your header comment
"""

# then any CONSTANT definitions

#then function definitions
#  First the function definition

def reverse_word(word):
    i = 0
    char_list = []
    while i < len(word):
        char_list.insert(0,word[i])
        i += 1
    return ''.join(char_list)

#NOW we'll put the main program

def mod_reverse_word(word):
    i = 0
    char_list =[]
    while i < len(word):
        char_list.insert(0, word[i])
        i += 1
    print (''.join(char_list))

def is_it_odd(num):
    #param: num is an integer; we will determine whether it is odd or even
    if num%2 == 0:
        return False
    else:
        return True
    print("Thank you for using this function")
    print("Isn't this fun? ")

def print_error_message(errno, errstring):
    #param: errno - the error number you've encountered
    #param: errstring - the string to tell the user about the error
    print("Error encountered")
    print("error number: ", errno, "specifically", errstring)

def get_scores():
    score = int(input("What was your grade on the exam?"))
    if score > 80:
        print_error_message(2, "That is too high to be a valid grade")
    project = int(input("What will your score on Project 1 be?"))
    if project < 95:
        print_error_message(1, "Don't sell yourself short")

if __name__ == "__main__":
    w = input("what word would you like reversed?")
    result = mod_reverse_word(w)
#    print(reverse_word(w))
    if result != None:
        print(result)
    else:
        print("Your function returned None")

score = int(input("What was your grade on the exam?"))
if score > 80:
    print_error_message(2,"That is too high to be a valid grade")
project = int(input("What will your score on Project 1 be?"))
if project < 95:
    print_error_message(1,"Don't sell yourself short")


#Call get_scores()
get_scores()