"""This program does basic math operations."""

firstnumber = 10
secondnumber = 5

# Printing some messages
print("Hello, World!")
print("Welcome to my simple Python program.")
print("Let's do some math operations.\n")

# Addition
sumresult = firstnumber + secondnumber
print("Addition of", firstnumber, "and", secondnumber, "is:", sumresult)

# Subtraction
subresult = firstnumber - secondnumber
print("Subtraction of", firstnumber, "and", secondnumber, "is:", subresult)

# Multiplication
mulresult = firstnumber * secondnumber
print("Multiplication of", firstnumber, "and", secondnumber, "is:", mulresult)

# Division
divresult = firstnumber / secondnumber
print("Division of", firstnumber, "and", secondnumber, "is:", divresult)

print("\nNow let's count numbers from 1 to 5.")

# Looping through numbers
for i in range(1, 6):
    print(i)

print("\nNow let's print a simple multiplication table for", firstnumber)

# Multiplication table
for i in range(1, 11):
    product = firstnumber * i
    print(f"{firstnumber} x {i} = {product}")

print("\nProgram finished successfully.")
