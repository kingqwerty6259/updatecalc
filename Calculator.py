import math

run = True
def math():
    answer = input("Enter expression to calculate: ")

    if answer.isalpha():
        return

    if " " in answer:
        answer = answer.split()
        num1 = answer[0]
        num2 = answer[2]
        operation = answer[1]
        if '.' in num1:
            num1 = float(num1)

        if '.' in num2:
            num2 = float(num2)

        if num1 != float(num1):
            num1 = int(num1)

        if num2 != float(num2):
            num2 = int(num2)

    if operation == "/":
        if num2 == 0:
            print("Can't divide by zero")
            return

    if (operation == "+"):
        print (num1, "+", num2, "=", num1 + num2)
    elif (operation == "-"):
        print (num1, "-", num2, "=", num1 - num2)
    elif (operation == "*"):
        print (num1, "x", num2, "=", num1 * num2)
    elif (operation == "/"):
        print(num1, "/", num2, "=", num1/num2)
while run == True:
    math()