#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))


# Example usage
a = 10
b = 2
division_result = safe_print_division(a, b)
print("Returned result:", division_result)
