import csv
total = 0
count = 0

with open("6.Read files/students.csv" , "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = total + float(row["Maths"])
        count = count + 1
    if count>0:
        average = total/count
        print("Average Math marks:" , average)