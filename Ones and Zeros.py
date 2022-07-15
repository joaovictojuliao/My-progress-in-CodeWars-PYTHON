def binary_array_to_number(arr):
    total = 0
    i = 1
    for num in arr[::-1]:
        total += (i*num)
        i *= 2
    return total
