"""
Sort the numbers in the list below.
"""
list_of_numbers = [1, 6, 3, 8, 3, 7, 2, 7, 0, 9]
list_of_numbers_copy = list.copy(list_of_numbers)
print(list_of_numbers)

print("Value at index 1 = " + str(list_of_numbers[1]))
print("Number of elements in list = " + str(len(list_of_numbers)))
print("\n")

for i in range(0, len(list_of_numbers) - 1):
    for j in range(0, len(list_of_numbers) - 1 - i):
        current_element = list_of_numbers[j]
        next_element = list_of_numbers[j + 1]
        print(str(list_of_numbers) + " Is Current Element: " + str(current_element) + " >  Next Element: " + str(
            next_element) + " " + str(current_element > next_element))
        if current_element > next_element:
            temp = list_of_numbers[j + 1]
            list_of_numbers[j + 1] = list_of_numbers[j]
            list_of_numbers[j] = temp

print("\nOriginal List: " + str(list_of_numbers_copy))
print("Sorted List: " + str(list_of_numbers))
