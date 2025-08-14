num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))

op = input("choose + or - : ")

if op == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif op == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
else:
    print("error")    