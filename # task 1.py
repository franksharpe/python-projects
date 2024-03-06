'''
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

# task 2 

first = str(input("what is your first name: "))
second = str(input("what is your second name: "))

print ("Hello "+ first + " " + second )

length = len(first + second)
print("Length of name: " + str(length))

reverse = input("would u like to see it backwards: (y/n) ")
if reverse == "y":
    print (first[::-1])
    print (second[::-1])
else:
    print("loser")
'''
#task 3

num = int(input("input a number"))
if num < 0:
    print("negtive")
elif num > 1:
    print("postive")
elif num == 0 :
    print("0")
    