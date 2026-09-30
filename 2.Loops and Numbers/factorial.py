num = int(input("enter a number:5"))
factorial = 1
for i in range(1 , num+1):
    factorial = factorial * i
print("Factorial of", num,  "is", factorial)