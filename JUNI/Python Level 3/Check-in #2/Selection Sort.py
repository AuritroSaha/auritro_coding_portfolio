#########################
# SELECTION SORT
#########################

# What is Selection Sort? Can you describe how it works by drawing out an example?

list1 = [2, 5, 10, 3, 6, 1]


# list1 = [1,2,5,10,3,6]
# list1 = [1,2,5,10,3,6]
# list1 = [1,2,3,5,10,6]
# list1 = [1,2,3,5,10,6]
# list1 = [1,2,3,5,6,10]

# What will list1 look after 2 passes of Selection Sort?
# Ans:

# The selectionSort() function below takes in a list and sorts the numbers from largest to smallest, but it's incomplete. Finish what's missing.
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


# What is the time complexity of Selection Sort? Can you describe the best and worst case scenarios?
# O(n^2)  Best = Worst
print(selectionSort(list1))