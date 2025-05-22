
num1 = float(input("enter first number:"))

num2 = float(input("enter second number:"))

operator = input("+,-,*,/")

if operator == '+':

    print(num1 + num2)

elif operator == '-':

    print(num1 - num2)
    
elif operator == '*':

    print(num1 * num2)

elif operator == '/':

    if num2 != 0:
        print(num1 /num2)
    else:
        print("false")
else:
    print("flse operator use +.-,*,/ operators only")

  




