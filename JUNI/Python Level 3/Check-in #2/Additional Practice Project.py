import random
import time
import copy


# Algorithm Comparison

# Copy in the code for each of the sorting functions that you have previously written, and write some tests to determine how fast each algorithm runs in a given scenario. Some possible scenarios to consider testing would be when the list to be sorted is already completely random, when it is already sorted, when it is sorted and reversed, and how many elements are in each of these lists (eg. n = 100, n = 1000, n = 2000, etc.). Can you think of any other scenarios?


# You can copy a list with this line of code: list2 = copy.deepcopy(list1)
# You can sort a list in reverse if you write list2.sort(reverse=True)

# Copy over your functions for insertion sort and selection sort here.

def insertionSort(lst):
    for i in range(len(lst)):
        j = i
        if len(lst[:j]) != 1:
            for n in range(j):
                if lst[j] < lst[j - 1]:
                    temp = lst[j - 1]
                    lst[j - 1] = lst[j]
                    lst[j] = temp
                    j = j - 1
    return lst


def selectionSort(lst):
    for i in range(len(lst)):
        maxItem = lst[i]
        maxItemI = i
        for j in range(i, len(lst)):
            if lst[j] > lst[maxItemI]:
                maxItem = lst[j]
                maxItemI = j
        lst.pop(maxItemI)
        lst.insert(i, maxItem)

    return lst


# create a variable for n

length = 4000

# generate a list with n random numbers in it

list1 = []

for i in range(length):
    list1.append(random.randint(0, 100))

# make 3 copies of the list with copy.deepcopy(list1)

list2 = copy.deepcopy(list1)
list3 = copy.deepcopy(list1)
list4 = copy.deepcopy(list1)
# sort and reverse two copies of the list with list3.sort(reverse=True)

list2.sort()
list3.sort(reverse=True)

# Find the times for all 4 tests (add more if you think of more scenarios)

print("Insertion Sort: ")
start = time.time()
insertionSort(list4)
end = time.time()
print("Random: " + str(end - start))
start = time.time()
insertionSort(list2)
end = time.time()
print("Sorted: " + str(end - start))
start = time.time()
insertionSort(list3)
end = time.time()
print("Reverse Sorted: " + str(end - start))

list2 = copy.deepcopy(list1)
list3 = copy.deepcopy(list1)
list4 = copy.deepcopy(list1)

list2.sort()
list3.sort(reverse=True)

print("Selection Sort: ")
start = time.time()
selectionSort(list4)
end = time.time()
print("Random: " + str(end - start))
start = time.time()
selectionSort(list2)
end = time.time()
print("Reverse Sorted: " + str(end - start))
start = time.time()
selectionSort(list3)
end = time.time()
print("Sorted: " + str(end - start))
