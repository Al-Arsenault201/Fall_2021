# in-class coding from Wednesday, October 27

def read_whole_file(fn):
    with open (fn,"r") as infile:
        s =infile.read()
#        print(s)
        list_of_nums = s.split()
        print(list_of_nums)

def read_file_as_lines(fn):
    with open(fn, "r") as newfile:
        s = newfile.readlines()
        print(s)

def read_a_line_at_a_time(fn):
    with open(fn) as thisfile:

        y = thisfile.readline()
        print(y)

if __name__ == "__main__":
#    file_to_read = "integers.txt"
    file_to_read = "/Users/alfredarsenault/PycharmProjects/integers.txt"
#    read_whole_file(file_to_read)
#    read_file_as_lines(file_to_read)
    read_a_line_at_a_time(file_to_read)


    with open("/Users/alfredarsenault/PycharmProjects/step_data.txt","r") as stepfile:
        j = stepfile.readline()
#        print(j)
        data = stepfile.read()
        print(data)
        # split the datastructure on newlines
        data.split('\n')
        print(data)
        input("press enter to continue")
        for i in range(len(data)):
            data[i].split()
 #           print(data[i])
            for j in len(data[i]):
                data[i][j] = int(data[i][j])
