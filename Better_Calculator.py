
num1 = float(input("Enter your first number: "))

num2 = float(input("Enter your second number: "))

op = input("Enter your operator: ")

if(op == "+"):
    print("Addition Result is ", num1 + num2)
elif(op == "-"):
    print("Subtraction Result is ",num1 - num2)
elif(op == "*"):
    print("Multiplication Result is ",num1 * num2)
elif(op == "/"):
    print("Division Result is ",num1 / num2)
else:
    print("You entered something wrong, Please check the opeator entered.")                