# Author: Terence Tang
# Date: 1/11/2021
# Description:  A program that takes an input file named data.txt and parses each line of integers into a sorted list
#               using the merge sort method.  For each input line of integers, the first int contains the length of the
#               set of numbers in the line.
#               Program outputs the resulting sorted lines of int in a file named merge.out

import time                                         # for tracking time needed for each algorithm to run
import random                                       # for random int creation


def generate_input(n):
    input = []
    for i in range(n):
        input.append(random.randint(-10000, 10000))
    return input


def mergesort(n):
    input = generate_input(n)
    length = n                                  # removes first int as length of set and updates list

    begin = time.perf_counter()  # sets initial start time
    sorted_list = merge_sort(input)                    # sorts set w/ insertion sort method
    sort_timer = time.perf_counter() - begin  # documents finish time and compares it to start time for run time

    return sort_timer


def merge_sort(input):
    length = len(input)
    if length == 1:                                         # base case for list of len 1, returns list
        return input
    else:                                                   # else splits lists into two halves and runs recursively
        a = merge_sort(input[0:int(length/2)])
        b = merge_sort(input[int(length/2):])
    return merge(a, b)                                      # once both halves are sorted, merges two halves together


def merge(a, b):
    results = []                                            # contains resulting sorted lists
    while (len(a) > 0 and len(b) > 0):                      # while neither set a or b is empty, selects smaller of the
        if (a[0] < b[0]):                                   # top integers from each list and appends to results
            results.append(a[0])
            a = a[1:]
        else:
            results.append(b[0])
            b = b[1:]

    while (len(a) > 0):                                     # when either list a or b is empty, takes the remainder of
        for num in a:                                       # the other list and appends it to results
            results.append(num)
            a = a[1:]

    while (len(b) > 0):
        for num in b:
            results.append(num)
            b = b[1:]

    return results                                          # returns the resulting sorted list


def main():
    test_cases = [1000, 5000, 10000, 15000, 20000, 25000, 30000]
    runs = 5
    for n in test_cases:                                    # runs the sort across multiple input sizes (n)
        avg_time = 0                                        # and several times for each size to get an avg sort time
        for i in range(runs):
            avg_time += mergesort(n)                        # runs insertion sort and returns the sort time
        avg_time = avg_time / runs                          # calculates avg sort time
        print("List Size: " + str(n) + ", Avg Merge Sorting Time: " + str(avg_time))

if __name__ == "__main__":  main()                          # allows for normal run procedure if file ran as script.
