import timeit
import itertools

def replace_zero(arr):

    # identify positions of 0's
    zeros = [i for i, num in enumerate(arr) if num==0]

    # setup
    max_seq = -1
    idx = -1

    for pos in zeros:
        # get copy of array and switch zeros to one each in turn
        check_arr = arr[:]
        check_arr[pos] = 1

        # calculate largest consecutive number of ones
        seq = max(len(list(v)) for g,v in itertools.groupby(check_arr) if g==1)

        # if result bested then update 
        if seq >= max_seq: 
            max_seq = seq
            idx = pos

        check_arr.clear()

    return idx

print(replace_zero([1,1,1,0,1,1,0,1,1,1]))
# print(replace_zero([0,1,0,0,0,0]))

# print(timeit.timeit(test, number=20000))
