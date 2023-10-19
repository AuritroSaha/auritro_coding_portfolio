# MERGE SORT

# What is Merge Sort? Can you describe how it works by drawing out an example?

# Would it make sense to ask what a list looks like after 2 passes of Merge Sort? What does it use in place of passes?

# The function merge() combines two sorted lists together, and is an important part in implementing Merge Sort in code. Finish the incomplete merge() function. Be sure to test the function after adding your code!
def merge(listA, listB):
    result = []
    while len(listA) > 0 and len(listB) > 0:
        if listA[0] > listB[0]:
            result.append(listB[0])
            listB.pop(0)
        elif listA[0] < listB[0]:
            result.append(listA[0])
            listA.pop(0)

    result = result + listA + listB

    return result


# Test your function here
A = [1, 2, 4, 7, 8, 10, 15]
B = [6, 9, 16, 19, 100]

print(merge(A, B))

# What is the time complexity of Merge Sort? Can you describe the best and worst case scenarios?

# O(n(log(n)))