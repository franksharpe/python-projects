#task 1 
a = int(input("Input first number: "))
print("")
print(str(a) + " is your first number")
b = int(input("Input second number: "))
print("")
print(str(b) + " is your second number")

print("What would you like to do?")

operation = input("Enter the operation you want to perform (floor division (//), modulus (%), exponentiation (**)): ")

if operation == "//":
    result = a // b
    print("The floor division result is:", result)
elif operation == "%":
    result = a % b
    print("The modulus result is:", result)
elif operation == "**":
    result = a ** b
    print("The exponentiation result is:", result)
else:
    print("Invalid operation selected")
