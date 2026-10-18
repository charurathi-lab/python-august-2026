numbers = [10,25,3,45,7,18]
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num>maximum:
        maximum = num
    if num<minimum:
        minimum = num
print("maximum:", maximum)
print("minimu:", minimum)