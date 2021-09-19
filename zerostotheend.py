def move_zeros(array):
    cnt_0 = array.count(0)
    array = [n for n in array if not n == 0]
    array.extend([0] * cnt_0)
    return array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))