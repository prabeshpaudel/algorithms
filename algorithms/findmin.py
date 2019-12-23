# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. 𝑂(𝑛2)
# O(n2). The second function should be linear 𝑂(𝑛).
import time

ls = [2,4,5,2,5,2,7,8,5,4,56,26,87,25,86,34,75,24,65,1,64,35, 34, 872, -2, 47, -34, 85, -332, 34, 5, 1, 4, 6 , 34, 34 ,65, 3]

def findMinOn(lst):
    min = lst[0]
    start_time = time.time()
    for i in lst:
        if i < min:
            min = i
    end_time = time.time()
    return min, end_time-start_time

def findMinOn2(lst):
    min = lst[0]
    start_time = time.time()
    for i in lst:
        isSmallest = True
        for j in lst:
            if i > j:
                isSmallest = False
        if isSmallest:
            min = i
    end_time = time.time()

    return min, end_time-start_time


print("O(n):  Min is %d and it required %10.7f seconds to run"%findMinOn(ls))
print("O(n2): Min is %d and it required %10.7f seconds to run"%findMinOn2(ls))


#Result:
# O(n):  Min is -332 and it required  0.0000019 seconds to run
# O(n2): Min is -332 and it required  0.0000501 seconds to run