def binary_search(array, element_to_search):
    left_index_position = 0
    right_index_position = len(array)
    mid_index_position = (left_index_position + right_index_position) // 2
    while left_index_position < right_index_position:
        if array[mid_index_position] > element_to_search:
            right_index_position = mid_index_position - 1
        elif array[mid_index_position] < element_to_search:
            left_index_position = mid_index_position + 1
        else:
            return "Element found in the list"
        mid_index_position = (left_index_position + right_index_position) // 2
    return "Element not found in the list"


element = [2, 3, 4, 12, 34, 89, 100]
element_to_search = 100
result = binary_search(element, element_to_search)
print(result)
element_to_search = 1
result = binary_search(element, element_to_search)
print(result)
