import csv
with open("6.Read files/student_records.csv" , "w" , newline = "") as file:
    writer = csv.writer(file)

    writer.writerow(["Name" , "Maths" , "Science", "English"])
    writer.writerow(["Aarav" , 85 , 90, 78])

print("Student record written successfully!")