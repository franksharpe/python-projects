#task 1 
a = int(input("input 1 number: "))
print("")
print(str(a) + " is your first number")
b = int(input("input 1 number: "))
print("")
print(str(a) + " is your 2nd number")

print("What would you like to do?")

c = input("Would you like to do floor division? (y/n): ")

if c == "y":
    result = a // b
    print("The floor division result is:", result)

