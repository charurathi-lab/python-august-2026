import json
with open("6.Read files/student.json" , "r") as file:
    student = json.load(file)
for student in student:
    print("name:" , student["name"])
    print("marks:" , student["marks"])
    print()
    