my_list = []

def display_menu():
    print("\nLIST OPERATIONS MENU")
    print("1. Add an element")
    print("2. Remove an element")
    print("3. Display the list")
    print("4. Clear the list")
    print("5. Exit")

def add_element():
    element = input("Enter the element to add: ")
    my_list.append(element)
    print(f"{element} has been added to the list.")

def remove_element():
    element = input("Enter the element to remove: ")
    if element in my_list:
        my_list.remove(element)
        print(f"{element} has been removed from the list.")
    else:
        print(f"{element} is not in the list.")

def display_list():
    print("The list elements are:", my_list)

def clear_list():
    my_list.clear()
    print("The list has been cleared.")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_element()
    elif choice == "2":
        remove_element()
    elif choice == "3":
        display_list()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        print("Exiting the program. Goodbye! ")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
