# Binary Search Algorithm
# To prove that binary search is faster than naive search
import time
import random

# Here in naive search we scan the whole list and ask if it is equal to the target
def NaiveSearch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Here in binary search we use divide and conquer
def BinarySearch(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low:
        return -1

    midPoint = (low + high) // 2

    if l[midPoint] == target:
        return midPoint
    elif target < l[midPoint]:
        return BinarySearch(l, target, low, midPoint-1)
    else:
        return BinarySearch(l, target, midPoint+1, high)

if __name__ == "__main__":
    #l = [23, 2, 55, 6, 7, 523, 5555]
    #target = 5555
    #print(NaiveSearch(l, target))
    #print(BinarySearch(l, target))

    # build a sorted list
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
       sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        NaiveSearch(sorted_list, target)
    end = time.time()
    print("Time Taken:", (end - start)/ length, "seconds")

    start = time.time()
    for target in sorted_list:
        NaiveSearch(sorted_list, target)
    end = time.time()
    print("Time Taken:", (end - start) / length, "seconds")


