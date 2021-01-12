def mergesort():
    input = []                                              # list to manage all lines from input file
    with open("data.txt",'r') as input_file:
        for line in input_file:                             # scans each line within input file
            line = list(map(int, line.split()))             # converts each line of str to a list of ints
            input.append(line)                              # appends each int set to inputs list
    input_file.close()

    # creates output file
    with open("merge.out", 'w') as output_file:            # opens the output file we will write to

        for line in input:                                  # for each int set from the inputs list
            length = line[0]                                # removes first int as length of set and updates list
            line = line[1:]

            line = merge_sort(line)                     # sorts set w/ insertion sort method

            # convert resulting line to string
            result = ''                                     # initializes output string
            count = 1
            for num in line:
                result += str(num)                          # converts each int in set to str value, adds to results
                if count < length:                         # fence posting statement for space char
                    result += " "
                count += 1

            # append line to output_file
            output_file.write(result)                       # appends resulting string line to output file
            output_file.write('\n')                         # adds a new line char for next set


def merge_sort(input):
    length = len(input)
    if length == 1:                                         # base case for list of len 1, returns list
        return input
    else:                                                   # else splits lists into two halves and runs recursively
        a = merge_sort(input[0:int(length/2)])
        b = merge_sort(input[int(length/2):])
    return merge(a, b)                                      # once both halves are sorted, merges two halves together


def merge(a, b):
    if len(a) == 0:                                         # base case for if half a is done, returns rest of half b
        return b
    elif len(b) == 0:                                       # base case for if half b is done, returns rest of half a
        return a
    elif a[0] < b[0]:                                       # if half a has the smaller top value, returns list that
        merge_results = merge(a[1:], b)                     # begins with smaller a value and a merged list consisting
        list = [a[0]]                                       # of the remainder of list a and all of list b
        for num in merge_results:                           # appends results to a new list return object
            list.append(int(num))
        return list
    else:                                                   # operates the same as if when list a is smaller, vice versa
        merge_results = merge(a, b[1:])
        list = [b[0]]
        for num in merge_results:
            list.append(int(num))
        return list


def main():
    mergesort()                                            # runs insertion sort and scans for input file


if __name__ == "__main__":  main()                          # allows for normal run procedure if file ran as script.
