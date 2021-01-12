# Author: Terence Tang
# Date: 1/11/2021
# Description:  A program that takes an input file named data.txt and parses each line of integers into a sorted list
#               using the insertion sort method.  For each input line of integers, the first int contains the length of
#               the set of numbers in the line.
#               Program outputs the resulting sorted lines of int in a file named insert.out

import time                                         # for tracking time needed for each algorithm to run
import random                                       # for random int creation


def generate_input(n):
    input = []
    for i in range(n):
        input.append(random.randint(-10000, 10000))
    return input


def insertsort(n):
    input = generate_input(n)
    length = n                                              # removes first int as length of set and updates list

    begin = time.perf_counter()                             # sets initial start time
    line = insertion_sort(input)                            # sorts set w/ insertion sort method
    sort_timer = time.perf_counter() - begin                # documents finish time and compares it to start time for run time

    return sort_timer


def insertion_sort(input):
    for index in range(1, len(input)):                      # iterates through list of items
        current = input[index]                              # pulls out the item we are sorting to re-insert
        pos = index - 1

        while pos >= 0 and input[pos] > current:            # shifts right all items that are larger volumes than index
            input[pos + 1] = input[pos]
            pos -= 1
        input[pos + 1] = current                            # re-inserts object once it's sorted
    return input


def main():
    test_cases = [1000, 5000, 10000, 15000, 20000, 25000, 30000]
    runs = 5
    for n in test_cases:                                    # runs the sort across multiple input sizes (n)
        avg_time = 0                                        # and several times for each size to get an avg sort time
        for i in range(runs):
            avg_time += insertsort(n)                       # runs insertion sort and returns the sort time
        avg_time = avg_time / runs                          # calculates avg sort time
        print("List Size: " + str(n) + ", Avg. Insertion Sorting Time: " + str(avg_time))

if __name__ == "__main__":  main()                          # allows for normal run procedure if file ran as script.
