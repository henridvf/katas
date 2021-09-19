def row_sum_odd_numbers(n):
    lst = [num for num in range(1, n * (n + 1)) if num % 2 != 0]
    return sum(lst[-n:])

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))