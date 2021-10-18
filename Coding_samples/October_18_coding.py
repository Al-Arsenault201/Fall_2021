# in-class coding for Monday, October 18

# main topic: multi-dimensional lists

medal_table = [
   [1,7,12,7, 26],
   [2,5,0,0,5],
   [3,4, 4, 2, 10],
   [4,4,2,3, 9],
   [5,4,1,4, 9]
]

#[[1,7,12,7,26],[2,5,0,0,5]]  don't do this

print(len(medal_table))  #number of rows

# how do I tell how many columns there are?
# each row can have a different length

RANK = 0
GOLDS = 1
SILVERS = 2
BRONZES = 3
TOTAL = 4

#"number of columns" in this table is meaningless
bad_medal_table = [
   [1,7,12,7, 26],
   [2,5,0,0],
   [3,4, 4, 2, 10],
   [4,2,3, 9],
   [5,4,1,4, 9]
]

#we can take the len() of a given row
print(len(medal_table[0]))
#syntax medal_table[i] tells which ROW we care about
#IF and ONLY IF all rows have the same number of elements can we
# meaningfully talk about COLUMNS

#how to reference an individual element
medal_table[ROW_NUMBER][COLUMN_NUMBER]

# of gold medals Poland won is
medal_table[3][1]

# all gold medals won
gold = 0
for i in range(len(medal_table)):
    gold += medal_table[i][1]
print(gold)

#using constants
gold = 0
for i in range(len(medal_table)):
    gold += medal_table[i][GOLDS]
print(gold)

gold = 0
for i in range(len(bad_medal_table)):
    gold += bad_medal_table[i][GOLDS]
print(gold)

#add a row - either append or insert
medal_table.append([6,2,3,3,8])


#I want to insert a column containing the country names
# want that to be column 1  - column 0 is rank; country next, then golds

countries = ['USA', 'Italy','Kenya','Poland','Jamaica','Netherlands']
for i in range(len(medal_table)):
    medal_table[i].insert(1,countries[i])


#inserting columns means I might have to change constants
GOLDS = 2
SILVERS = 3
BRONZES = 4
TOTAL = 5


#creating a new 2D list from scratch
#write a routine that fills a 2D table with the
#successive squares - 1, 4, 9, 16, 25,...
ROWS = 5
COLUMNS = 10
table_of_squares = []  #create the initial blank table
num_to_be_squared = 1
for i in range(ROWS):
   row = []  #create a new 1-d list

   #build one row

   for j in range(COLUMNS):
       row.append(num_to_be_squared**2)
       num_to_be_squared += 1
#       print("row", i, "=",row)

   #now add that one row to the 2-D list
   table_of_squares.append(row)
#print(table_of_squares)

#pretty-print
for i in range(len(table_of_squares)):
    print(table_of_squares[i])


