num1 = int(input("Enter the first number"))
num2 = int(input("Enter second number"))
op = input("Enter operator")

if op == " + ":
    print(num1+num2)
elif op == "-":
    print("The subraction is", num1-num2)
elif op == "*":
    print("The multiplication is ",num1*num2)
elif op == "/":
    print("The division is", num1/num2)
else:
    print("Invalid operator")


