def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers)<2:
        return None
    else:
        unique_numbers.sort()
        return unique_numbers[-2]
lst = [1,5,88,93,24,66,99,88,5,1]
print(second_largest(lst))