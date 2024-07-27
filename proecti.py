#kalkulatori
print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

a = input()
if a =="1":
    num1 =int( input("enter first number: "))
    num2 =int( input("enter second number: "))
    print("answer is "+ str(num1 + num2))

elif a =="2":
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    print("answer is "+ str(num1 - num2))
elif a =="3":
    num1 =int( input("enter first number: "))
    num2 =int( input("enter second number: "))
    print("answer is "+ str(num1 * num2))
elif a =="4":
    num1 =int( input("enter first number: "))
    num2 =int( input("enter second  number: "))
    print("answer is "+ str(num1 // num2))
else:
    print("invalid enter ")

