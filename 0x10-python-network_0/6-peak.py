#!/usr/bin/python3
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        current_element = list_of_integers[mid]

        # Check if the current element is greater than its neighbors
        if current_element > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]

# Example usage:
my_list = [1, 3, 20, 4, 1, 0]
peak = find_peak(my_list)
print("Peak:", peak)
