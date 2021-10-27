
if __name__ == "__main__":

    with open("/Users/alfredarsenault/PycharmProjects/step_data.txt","r") as stepfile:
        j = stepfile.readline()
#        print(j)
        data = stepfile.read()
        print(data)
#        input("press to continue")
        # split the datastructure on newlines
        data = data.split('\n')
#        print(data)
#        input("press enter to continue")
        for i in range(len(data)):
            data[i] = data[i].split()
#            print(data[i])
            for j in range(len(data[i])):
                data[i][j] = int(data[i][j])
        print(data)

#now calculate September calories burned. That is stored in column 1 of each row
    total_calories_September = 0
#    print(len(data))
    for i in range(len(data)-1):
        total_calories_September += data[i][1]
    ave_calories_September = total_calories_September / len(data)

# now do the same for October. That's in column 3 of each row
    total_calories_October = 0
    for i in range(len(data)-1):
        total_calories_October += data[i][3]
    ave_calories_October = total_calories_October /len(data)

    print("September calories were ", total_calories_September, end = " ")
    print("for an average of ", ave_calories_September, " calories per day")

    print("October calories were ", total_calories_October, end=" ")
    print("for an average of ", ave_calories_October, " calories per day")

