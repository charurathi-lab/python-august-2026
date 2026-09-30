num1 =  int(input("enter the first number:"))
num2 = int(input("enter the second number: "))
operator = input("choose an operator'+' '-' *' '/' : ")
if operator == '+':
    sum= num1 + num2
    print("sum is" ,sum)
elif operator == '-':
    diff = num1 - num2
    print("Difference is" , diff)
elif operator ==  '*':
    pro = num1 * num2
    print("Product is" , pro)
else:
    quo = num1/num2
    print("quotient is", quo)
