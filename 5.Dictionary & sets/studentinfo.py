student = {
    "roll_no": 101,
    "name": "Aarav Sharma",
    "age": 19,
    "grade": "A+",
    "subjects":["Math", "Physics", "Computer Science"]
}

print("----------------")
print(" STUDENT INFORMATION ")
print("Roll Number:", student["roll_no"])
print("Name :" , student["name"])
print("Age:", student["age"])
print("Grade :" , student["grade"])
print("Subjects:", ",".join(student["subjects"]))
