def display_menu():
    print("\nOPERATOR MENU")
    print("1. Arithmetic Operators")
    print("2. Relational Operators")
    print("3. Logical Operators")
    print("4. Exit")

def arithmetic_operators(a, b):
    print(f"\na = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")

def relational_operators(a, b):
    print(f"\na = {a}, b = {b}")
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a > b: {a > b}")
    print(f"a < b: {a < b}")
    print(f"a >= b: {a >= b}")
    print(f"a <= b: {a <= b}")

def logical_operators(a, b):
    print(f"\na = {a}, b = {b}")
    print(f"a and b: {a and b}")
    print(f"a or b: {a or b}")
    print(f"not a: {not a}")

while True:
    try:
        a = int(input("\nEnter value for a: "))
        b = int(input("Enter value for b: "))
    except ValueError:
        print("Invalid input! Please enter integer values.")
        continue
    
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        arithmetic_operators(a, b)
    elif choice == "2":
        relational_operators(a, b)
    elif choice == "3":
        logical_operators(a, b)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
