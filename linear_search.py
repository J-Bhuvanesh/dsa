def linear_search(element, element_to_search):
    for ele in element:
        if ele == element_to_search:
            return "Element found in a list"
    return "Element not found in the list"


element = [2, 3, 467, 89, 12, 34, 5, 6, 7]
element_to_search = 7
result = linear_search(element, element_to_search)
print(result)
element_to_search = 1
result = linear_search(element, element_to_search)
print(result)
