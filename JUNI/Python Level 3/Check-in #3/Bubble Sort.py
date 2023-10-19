# BUBBLE SORT

# What is Bubble Sort? Can you describe how it works?

list1 = [4, 8, 2, 1, 10, 0]


# What does the list1 look like after 2 passes of Bubble Sort?
# ans: [4,2,1,8,0,10]
#      [2,1,4,0,8,10]

# Finish the incomplete bubbleSort() function. Be sure to test the function after adding your code!
def bubbleSort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


print(bubbleSort(list1))

# What is the time complexity of Bubble Sort? Can you describe the best and worst case scenarios? 