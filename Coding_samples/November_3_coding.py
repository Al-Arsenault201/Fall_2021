# in-class coding for Wednesday, November 3

dogs = {}
dogs['doug'] = ['beagle','bulldog']

dogs['lizzie'] = 'Australian cattle dog'

if dogs.get('Bentley') == None:
    print("error - missing dog")
else:
    print(dogs['Bentley'])

print (dogs.get('Bentley', "error-missing dog"))

# change the value associated with a key
#easiest way - use a new assignment statement
dogs['doug'] = ['beagle','boxer']


# depending on the type of the value, we can use defined methods to change the value
# if the value is a list, we can use remove, pop, append, insert, to change values


#keys() returns a view object with a list of all the keys in the dictionary
#values() returns a view object with list of all the values in the dictionary

#what's a view object?
cars = {}
cars['year'] = 2006
cars['make'] = 'Toyota'
cars['model'] = 'Corolla'
cars['mileage'] = 257000

cars['color'] = 'tan'

cars.values()

if 'year' in cars.keys():
    print("The model year is ", cars['year'])
else:
    print("Error - there is no year in the dictionary")


for f in cars.keys():
    print("The next key is ", f)

for v in cars.values():
    print("The value is ", v)

#mapping keys to values
for f in cars.keys():
    print("for key ", f, " the value is ", cars[f])


#you cannot go backwards
# you can know that a value is in the dictionary:
for x in cars.values():
    #we know the value is in the dictionary; we can't directly get the associated key
    # we have to check each key to find the one with the right value
    for y in cars.keys():
        if cars[y]== x:
            print("The key for value ", x, "  is ", y)


#dictionary where keys are integers
floors = {0:'basement',1:'lobby', 2:'mezzanine', 3:'AmEx', 4:'AmEx',5:'CMSC',6:"Instrumental music"}


# creating dictionary by zipping two lists

a = [1,2,3]
b = ['a','b','c']
d = dict(zip(a,b))

# what happens if the lists are of different lengths?
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']
d = dict(zip(a,b))

# and
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd','e']
d = dict(zip(a,b))
