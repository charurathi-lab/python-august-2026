num1 = int(input("Enter a number:"))
num2 = int(input("enter the second number:"))
operator= input("Choose an operator '+', '-', '*' , '/' :")
if operator == '+':
    sum = num1 + num2
    print("sum is", sum)
elif operator == '-':
    diff = num1 - num2
    print("Difference is", diff)
elif operator == '*' :
    pro = num1 * num2
    print("Product is" , pro)
else :
    quo = num1/num2
    print("Quotient is" , quo)
