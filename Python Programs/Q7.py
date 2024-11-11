import random

def generate_random_number(lower, upper):
    return random.randint(lower, upper)

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

random_number = generate_random_number(lower_limit, upper_limit)
print(f"Random number among {lower_limit} and {upper_limit}: {random_number}")
