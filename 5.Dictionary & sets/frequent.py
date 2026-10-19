#most frequent element
numbers = [1,2,3,2,4,2,5,3]
most_frequent = numbers[0]
max_count = 0
for num in numbers:
    count = numbers.count(num)
    if count>max_count:
        max_count = count
        most_frequent = num
print("Most frequent element:", most_frequent)
print("Frequency:", max_count)