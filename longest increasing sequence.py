def maxSeq(data):
    maxSeq = 0
    newSeq = 1
    for i in range (len(data)):
        if newSeq > maxSeq:
            maxSeq = newSeq
        if len(data) == 1:
            maxSeq = newSeq
            pass
        if i == len(data)-1:
            pass
        else:               
            x = int(data[i])
            y = int(data[i+1])
            if y > x:
                newSeq += 1
            else:
                newSeq = 1
    return maxSeq


def do_one_test(data):
    print("The max subsequence of {} has length {}".format(data, maxSeq(data)))
    pass

def main():
    do_one_test([])
    do_one_test([1])
    do_one_test([1, 2, 3])
    do_one_test([1, 1, 1])
    do_one_test([1, 2, 1, 2, 3, 4, 1, 2])
    do_one_test([-2, -1, 0, 1, 2])
    do_one_test([1, 2, 3, 1, 2, 3, 4])
    do_one_test([1, 2, 3, 4, 1, 2, 3])
    do_one_test([-10, -4, 0, 5, 34, 89])
    do_one_test([3, 0, 4, 5])
    do_one_test([3, 5, -12])
    do_one_test([1, 2, 1, 3, 5, 6, 2, 5, 8, 12])
    do_one_test([1, 2, 1, 5, 5, 6, 7, 9, 7, 5, 12])
    pass

if __name__ == "__main__":
    main()
    pass
