def insertsort():
    input = []                                              # list to manage all lines from input file
    with open("data.txt",'r') as input_file:
        for line in input_file:                             # scans each line within input file
            line = list(map(int, line.split()))             # converts each line of str to a list of ints
            input.append(line)                              # appends each int set to inputs list
    input_file.close()

    # creates output file
    with open("insert.out", 'w') as output_file:            # opens the output file we will write to

        for line in input:                                  # for each int set from the inputs list
            length = line[0]                                # removes first int as length of set and updates list
            line = line[1:]

            line = insertion_sort(line)                     # sorts set w/ insertion sort method

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
    insertsort()                                            # runs insertion sort and scans for input file


if __name__ == "__main__":  main()                          # allows for normal run procedure if file ran as script.
