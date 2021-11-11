#in class coding from November 10

def palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return palindrome(word[1:-1])




if __name__ == "__main__":
    phrase = input("Enter the phrase to check")
    print(palindrome(phrase))


    s = "012345678"
    for i in range(len(s)):
        print(s[i])

        #how would I get rid of s[0] and s[8]?

        #just keep s[1] through s[7]
        s[1:8]
        #the last character is also always -1

#summing the values in a list of integers
def recursively_sum_list (l):
    if len(l) == 0:
        return 0
    else:
        value = l[0]
        new_l = l[1:]
        return value + recursively_sum_list[new_l]


import new_p2_demo
db = read_a_file("/Users/alfredarsenault/Documents/Fall_2021_Project_2/Fall_2023.csv")
print(db)

