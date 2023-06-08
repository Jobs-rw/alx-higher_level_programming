#!/usr/bin/python3
# Importing specific functions from the calculator_1 module
from calculator_1 import add, subtract, multiply, divide

# Define variables a and b
a = 10
b = 5

# Call the imported functions with variables a and b as arguments
sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
quot_result = divide(a, b)

# Print the results
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Quotient:", quot_result)
