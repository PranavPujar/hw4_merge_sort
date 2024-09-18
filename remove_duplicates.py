def remove_duplicates(array):
    if not array:
        return []

    unique = [array[0]]
    for i in range(1, len(array)):
        if array[i] != array[i-1]:
            unique.append(array[i])

    return unique

# Example usage
array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
result = remove_duplicates(array)
print(result)