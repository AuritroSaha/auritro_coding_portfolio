# Binary Search

# What is Binary Search? When can we use it? What are the two ways we can implement it? Can you describe how it works by drawing out an example?


# The binarySearch() function takes in a list and sorts the numbers from largest to smallest, but it's incomplete. Fill in the missing code to create two working Binary Search functions, one that works iteratively and one that works recursively. Be sure to test the function after adding your code!
def binSearchIter(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (high + low) // 2
        x = lst[mid]

        if x == item:
            return True
        elif x < item:
            low = mid + 1
        else:
            high = mid - 1

    return False


# def binSearchRecur(lst, item):
#     high = len(lst) - 1
#
#     if high < 0:
#         return False
#
#     mid = high // 2
#
#     if lst[mid] == item:
#         return True
#     elif lst[mid] < item:
#         binSearchRecur(lst(mid:), item)
#         else:
#         binSearchRecur(lst(:mid), item)

        # O(logn) Best: middle is the item   Worst: item doesn't exist