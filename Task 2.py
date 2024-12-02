#Task 2 : Calculator
print("Task 2 : Calculator")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Enter numeric values.")
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
choice = input("Enter your choice: ")
if choice == '1':
    print(num1 ,"+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1 ,"-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1 ,"*", num2, "=", num1 * num2)
elif choice == '4':
    if num2 == 0:
        print("ZeroDivisionError")
    else:
        print(num1 ,"/", num2, "=", num1 / num2) 
else:
    print("Please choose a valid operation(1 to 4).")