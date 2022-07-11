def task(array):
    left = -1
    right = len(array)
    while (right - left > 1):
        middle = (left + right) // 2
        if array[middle] == '0':
            right = middle
        else:
            left = middle
    return right


assert task("000000000") == 0
assert task("1000000000") == 1
assert task("111111111000000000") == 9
assert task("11111111111000000000") == 11
assert task("1111111111111111111000000000") == 19
