from asyncio import base_tasks
from cmath import log
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def main():
    # arr = [[6, 'THE'], [3, 'THIS'], [9, "YAY!!!"], [4, 'IS'], [7, 'CORRECT'], [2, 'LOOK'], [8, 'SORT'], [1, "HEY"]]
    # print(radixSort(16, 8, arr))
    # print(mergeSort(arr)) 

    file = open('results.md', 'w')
    for i in range(1, 17):
        n = pow(2, i)
        file.write("\n--- n = 2^" + str(i) + " ---\n")
        for j in range(0, 21):
            u = pow(2, j)
            radixSum = 0
            mergeSum = 0
            countSum = 0

            for _ in range(0, 11):
                arr = [[random.randint(0, u - 1), 'value'] for _ in range(n)]

                start = time.time()
                radixSort(u, n, arr)
                end = time.time()
                radixSum += end - start

                start = time.time()
                mergeSort(arr)
                end = time.time()
                mergeSum += end - start

                start = time.time()
                countSort(u, arr)
                end = time.time()
                countSum += end - start

                radixAvg = radixSum/10
                mergeAvg = mergeSum/10
                countAvg = countSum/10

            smallest = min(radixAvg, mergeAvg, countAvg)
            winner = "R" if radixAvg == smallest else "M" if mergeAvg == smallest else "C" if countAvg == smallest else '?'
            file.write("U = 2^" + str(j) + " " + winner + "\n")

        # print("RadixSort: ", radixSum / 10)
        # print("MergeSort: ", mergeSum / 10)
        # print("CountSort: ", countSum / 10)
    file.close()
    return

def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    n = len(arr)
    k = math.ceil((log(univsize, 2) / log(base, 2)).real)
    for i in range (0, n):
        arr[i][1] = [arr[i][1], BC(arr[i][0], base, k)]

    for j in range (0, k):
        for i in range(0, n):
            arr[i][0] = arr[i][1][1][j]
        arr = countSort(base, arr)
        
    for i in range(0, n):
        sum = 0
        for num in range(0, len(arr[i][1][1])):
            sum += arr[i][1][1][num] * pow(base, num)
        arr[i] = [sum, arr[i][1][0]]
    
    return arr

if __name__ == "__main__":
    main()
    




