# in-class coding from Wednesday, December 8

# analyzing performance of different sorting algorithms
import random
import time

def generate_random_list(length):
    list = [ ]
    for i in range(length):
        list.append(random.randint(1,100))
    return list

def bubble_sort (numbers):
# go through the entire list of numbers
    start = time.time()
    comparisons = 0
    swaps = 0
    for i in range(len(numbers)-1,0, -1):
       for j in range(i):
           comparisons += 1
           if (numbers[j] > numbers[j + 1]):
               # swap the numbers - we'll use a temp
               swaps += 1
               temp = numbers[j]
               numbers[j] = numbers[j + 1]
               numbers[j + 1] = temp
    print("This took ", comparisons, " comparisons and ", swaps, " swaps" )
    end = time.time()
    print("This took ", end-start)
    return (numbers)

def selection_sort(numbers):
    comparisons = 0
    swaps = 0
    for i in range(len(numbers)):

            # find the smallest element remaining in the
            # unsorted list. Start by presuming it's the
            # first element
            smallest = i
            for j in range(i + 1, len(numbers)):
                comparisons += 1
                if numbers[smallest] > numbers[j]:
                    smallest = j

            # When the loop is done, we know that smallest is
            # the index of the smallest value. Swap it
            # with the first element
            swaps += 1
            temp = numbers[smallest]
            numbers[smallest] = numbers[i]
            numbers[i] = temp
    print("this process took ", comparisons ," comparisons and ", swaps, " swaps")
    return numbers

def quicksort(list_of_nums):
#    print(list_of_nums)
    # base case - a list of length one is sorted
    if len(list_of_nums) <= 1:
        return (list_of_nums)
        # recursive case
    else:
            # pick a pivot - the first element
        pivot = list_of_nums[0]
        # define three empty lists, for elements greater than the pivot, less than the pivot, and equal to the pivot

        less = []
        equal = []
        greater = []
    # go through the list and put each element in the proper list
        for i in range(len(list_of_nums)):

            if list_of_nums[i] > pivot:

                greater.append(list_of_nums[i])
            elif list_of_nums[i] == pivot:
                equal.append(list_of_nums[i])
            else:

                less.append(list_of_nums[i])
        results =quicksort(less) + equal + quicksort(greater)
        return(results)

if __name__ == "__main__":
    l = generate_random_list(20000)
#    print(l)
#    sorted_l = bubble_sort(l)
#print(sorted_l)
#    start = time.time()
#    sl = selection_sort(l)
#    end = time.time()
#    elapsed_time = end - start
#    print(elapsed_time)
#    print(sl)

    start = time.time()
    ql = quicksort(l)
    end = time.time()
    elapsed_time = end - start
    print(elapsed_time)
    print(ql)