# in-class coding for Monday, October 4

news = input("Enter the headline from today's news")

news = news.strip()
print(news)


#define four numbers: Pn, Pn1, Pn2, Pn3
#start with 1,1,and 1
Pn1 = 1
Pn2 = 1
Pn3 = 1
Pn = 2
#prompt for the goal
goal = ...#you know how to write this
while not(Pn) >= goal:
    Pn3 = Pn2
    Pn2 = Pn1
    Pn1 = Pn
    Pn = Pn2 + Pn3


#problem 3

"""
Header comment for problem 3
"""

import sys
from random import choice, seed

if len(sys.argv) >= 2:
   seed(sys.argv[1])

if __name__ == "__main__":
    #put your program here


#problem 5

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

num = int(input....)

if num%PRIMES[i] == 0:
    #divide num by PRIMES[i]
    #test again - is num%PRIMES[i] == 0...

news = input("Please enter today's headlines")

    # get rid of extra whitespace
news = news.strip()
words = news.split()

instring = input("Type in words separated by commas")
wordlist = instring.split(',')
reversed_list=[]
for i in range(len(wordlist)):
    reversed_list.append(wordlist[len(wordlist)-(i+1)])
print(reversed_list)

newstring = "".join(reversed_list)
commastring = ",".join(reversed_list)

#print a table of the first 100 squares
# 10 to a row, 10 rows

for i in range(10):
    for j in range(10):
        print((j + i*10)**2,end = ' ')
    print('\n')