my_tuple = ()

def display_menu():
    print("\nTUPLE OPERATIONS MENU")
    print("1. Create a new tuple")
    print("2. Display the tuple")
    print("3. Clear the tuple")
    print("4. Exit")

def create_tuple():
    global my_tuple
    elements = input("Enter elements separated by commas: ").split(",")
    my_tuple = tuple(elements)
    print("New tuple created.")

def display_tuple():
    print("The tuple elements are:", my_tuple)

def clear_tuple():
    global my_tuple
    my_tuple = ()
    print("The tuple has been cleared.")


while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        create_tuple()
    elif choice == "2":
        display_tuple()
    elif choice == "3":
        clear_tuple()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
