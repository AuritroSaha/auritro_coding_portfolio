def f1(n):
    for i in range(n):
        print(i)

        # O(n):


def f2(n):
    for i in range(n // 2):
        print(i)

        # O(n):


def f3(n):
    k = 0
    for i in range(n // 2):
        for j in range(n // 4):
            k += 1
            print(k)

            # O(n^2): print runs n/4 times in inner loop. Inner loop runs n/2 times. print runs n/2 * n/4 = n^2/8 in total


def f4(n):
    k = 0
    for i in range(n):
        for j in range(i):
            k += 1
            print(k)  # runs as i changes: 0 + 1 + 2 + 3 + 4 + ... + (n - 1)

            # 0(n^2): print runs i times in inner loop and the inner loop runs n times in the outer loop


def f5(n):
    if (n <= 0):
        return
    else:
        print(n)
        f5(n - 1)

        # O(n): it runs n times because it subtracts 1 everytime and stops when n = 0


def f6(n):
    if (n == 1):
        return
    else:
        print(n)
        f6(n // 2)

        # f6(n) = 1 + f6(n//2); f(1) = 0
        # O(infinite): any even number divided by 2 enough times will become odd and therefore will never reach 1 unless the number starts off as 2 100/2/2 = 25, 40/2/2/2 = 5, 2/2 = 1


def f7(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
                return

                # O(1): no matter what number any variable is it will run once because it returns on the first loop of each loop


def f8(n, m):
    for i in range(n):
        print(i)
    for i in range(m):
        print(i)

        # O(n+m)


def f9(n, m):
    for i in range(m):
        for j in range(n):
            print(i, j)

            # O(nm)


def f10(n, m):
    for i in range(m):
        for j in range(n):
            print(i, j)
        return

    # O(n)


""" For the list problems below: assume the length list is N
    Note: all lists are of INTEGERS (this includes negative numbers and zero) """


def f11(lst):
    for item in lst:
        print(item)

        # O(n)


def f12(lst):
    n = len(lst)
    for i in range(n):
        item1 = lst[i]
        for j in range(n):
            item2 = lst[j]
            if i == j:
                continue
            if item1 == item2:
                return True
    return False

    # O(n^2)


def f13(lst):
    for item in lst:
        if item == 0:
            return True
    return False

    # O(n)


def f14(lst):
    for item in lst:
        if item == 1:
            return True
    return False

    # O(n)