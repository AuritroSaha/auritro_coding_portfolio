#########################
# TIME COMPLEXITY
#########################

# What is Big-O analysis?

# Find the Big-O of each of these functions:
# 1. f(n) = n^2 + 1000n         O(n^2)
# 2. f(n) = log(n) + sqrt(n)    O(sqrt(n))
# 3. f(n) = 1*2*3*4*...*n       O(n!)

# Look at the definition of weirdFunction. What is the best case scenario? What is the worst case scenario? What is the Big-O of weirdFunction?
def weirdFunction(nums):
    if len(nums) % 2 == 1:
        print("There are an odd amount of numbers")
    else:
        for i in range(len(nums)):
            print(i, nums[i])


# Best case: odd amount of numbers  Worst: Even amount of numbers   O(n)

# What is the time complexity of function1? Let n be the length of nums.
def function1(nums):
    for num in nums:
        for i in range(3):
            print(i, num)


# function1([12,45,23,67])

# O(n)

# What is the time complexity of function2?
def function2(n):
    print(n)
    if n > 2:
        function2(n // 2)


# function2(50)

50, 25, 12, 6, 3, 1
48, 24, 12, 6, 3, 1