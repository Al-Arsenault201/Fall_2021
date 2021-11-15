#function volume
def vol(height, radius):
    return(height * (radius**2)* 3.14159)

s = "Probably Secure Operating System"
list_s = s.split()
list_s[0] = "Provably"
new_s = " ".join(list_s)

s = "Probably Secure Operating System"
list_s = []
for i in s:
    list_s.append(i)

for i in range(len(s)):
    list_s.append(s[i])


list_s[3] = 'v'
new_s = "".join(list_s)

table = []
for i in range(10):  # for each row
#build one row
    new_row = []
    for j in range(10):
        new_row.append(10*i + j)
# add the new row to the table
    table.append(new_row)
    print(table)
    input("press enter to continue")


with open("/Users/alfredarsenault/cities.txt","r") as infile:
    data = infile.read()
    print(data)
    new_data = data.split("\n")
    for i in range(len(new_data)):
        new_data[i] = new_data[i].split()  #split("\t")
    total = 0
    for i in range(len(new_data)):
#        print(new_data[i][1])
        total += int(new_data[i][1])
    ave = total/len(new_data)
    print("The average population is", ave)


def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[:-1])  # this chops off last character of the string = s[1:] chops off first letter

if __name__ == "__main__":
    s = "supercalifragilisticexpialidocius"
    print(string_length(s))


d = {}
s = input("Please enter the key for the next entry. Type 'Q' to quit")
while s != 'Q':
    v = input("Please enter the value for this key")
    d[s] = v
    s = input("Please enter the key for the next entry. Type 'Q' to quit")

