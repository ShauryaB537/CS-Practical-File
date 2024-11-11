x = 10 # Global variable

def func():
    y=5 # Local variable (only accessible within this function)

    global x
    x = x + y  # Now x will be modified globally

    print("\nInside function:")
    print("Global variable x:", x)  # Modified global variable
    print("Local variable y:", y)   # Local variable

func()

# Outside the function
print("\nOutside function:")
print("Global variable x:", x)
