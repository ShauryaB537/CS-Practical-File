my_dict = {}

def display_menu():
    print("\nDICTIONARY OPERATIONS MENU")
    print("1. Add a key-value pair")
    print("2. Remove a key-value pair")
    print("3. Display the dictionary")
    print("4. Clear the dictionary")
    print("5. Exit")

def add_key_value():
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
    print(f"Key-value pair ({key}: {value}) has been added to the dictionary.")

def remove_key_value():
    key = input("Enter the key to remove: ")
    if key in my_dict:
        del my_dict[key]
        print(f"Key {key} and its associated value have been removed.")
    else:
        print(f"Key {key} is not in the dictionary.")

def display_dictionary():
    print("The dictionary is:", my_dict)

def clear_dictionary():
    my_dict.clear()
    print("The dictionary has been cleared.")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_key_value()
    elif choice == "2":
        remove_key_value()
    elif choice == "3":
        display_dictionary()
    elif choice == "4":
        clear_dictionary()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
