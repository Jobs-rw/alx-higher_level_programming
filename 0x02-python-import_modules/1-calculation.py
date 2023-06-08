#!/usr/bin/python3
# Importing specific functions from the calculator_1 module
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    # Define variables a and b
    a = 10
    b = 5
    # Call the imported functions with variables a and b as arguments
    sum_result = add(a, b)
    diff_result = subtract(a, b)
    prod_result = multiply(a, b)
    quot_result = divide(a, b)
    print('{} + {} = {}'.format(a, b, sum_result))
    print('{} - {} = {}'.format(a, b, diff_result))
    print('{} * {} = {}'.format(a, b, prod_result))
    print('{} + {} = {}'.format(a, b, quot_result))
