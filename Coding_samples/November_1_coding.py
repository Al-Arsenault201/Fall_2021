# in-class coding from Monday, November 1

# more on reading files

if __name__ == "__main__":
    with open("/Users/alfredarsenault/Downloads/September - Sheet1.csv", "r") as stepfile:
        j = stepfile.readline()
        data = stepfile.readlines()
#        print(data)
        for i in range(len(data)):
            data[i] = data[i].split(',')
#        print(data)
            while '' in data[i]:
                data[i].remove('')
            for k in range(len(data[i])):
                data[i][k] = int(data[i][k])
        print(data)



#now calculate September calories burned. That is stored in column 1 of each row
    total_calories_September = 0
#    print(len(data))
    for i in range(len(data)):
        total_calories_September += data[i][1]
    ave_calories_September = total_calories_September / len(data)

# now do the same for October. That's in column 3 of each row
    total_calories_October = 0
    for i in range(len(data)):
        total_calories_October += data[i][3]
    ave_calories_October = total_calories_October /len(data)


#change print to write to write file

    with open("/Users/alfredarsenault/PycharmProjects/results.txt","w") as outfile:
        answer = "September calories were " + str(total_calories_September) + "for an average of "+ str(ave_calories_September) + " calories per day" + '\n' + "October calories were " + str(total_calories_October) + "for an average of " + str(ave_calories_October) + " calories per day"
        outfile.write(answer)
#    print(answer)


###
# this part is on dictionaries
# create a dictionary of dogs
#name, breed

dogs ={'doug':['beagle','bulldog'],'lizzie':"Australian Cattle Dog" }
dogs['bentley'] = 'golden retriever'

# to access an element of the dictionary - dictionary name [ key]

#if that key does not exist, python adds that element to the dictionary
dogs['bonnie'] = 'beagle'
dogs ['baron'] = 'beagle'

# len returns the number of keys

