#########################
# INSERTION SORT
#########################

# What is Insertion Sort? Can you describe how it works by drawing out an example?

list2 = [3, 7, 2, 5, 10, 1]
# What will list2 look like after 3 passes of Insertion Sort?
  # Ans: [3, 7, 2, 5, 10, 1]
        #[3, 7, 2, 5, 10, 1]
        #[2, 3, 7, 5, 10, 1]

# Finish the incomplete insertionSort() function below
def insertionSort(lst):
  for i in range(len(lst)):
    j = i
    if len(lst[:j]) != 1:
      for n in range(j):
        if lst[j] < lst[j-1]:
          temp = lst[j-1]
          lst[j-1] = lst[j]
          lst[j] = temp
          j = j-1
  return lst

print(insertionSort(list2))

# What is the time complexity of Insertion Sort? Can you describe the best and worst case scenarios?
