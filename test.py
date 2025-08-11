"""This program does basic math operations."""

first_number = 10
second_number = 5

# Printing some messages
print("Hello, World!")
print("Welcome to my simple Python program.")
print("Let's do some math operations.\n")

# Addition
sum_result = first_number + second_number
print("Addition of", first_number, "and", second_number, "is:", sum_result)

# Subtraction
sub_result = first_number - second_number
print("Subtraction of", first_number, "and", second_number, "is:", sub_result)

# Multiplication
mul_result = first_number * second_number
print("Multiplication of", first_number, "and", second_number, "is:", mul_result)

# Division
div_result = first_number / second_number
print("Division of", first_number, "and", second_number, "is:", div_result)

print("\nNow let's count numbers from 1 to 5.")

# Looping through numbers
for i in range(1, 6):
    print(i)

print("\nNow let's print a simple multiplication table for", first_number)

# Multiplication table
for i in range(1, 11):
    product = first_number * i
    print(f"{first_number} x {i} = {product}")

print("\nProgram finished successfully.")
