import heapq

def merge_k_sorted_arrays(arrays):
    result = []
    min_heap = []

    # Add the first element from each array to the min heap
    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))

    # Process elements from the min heap
    while min_heap:
        val, array_index, element_index = heapq.heappop(min_heap)
        result.append(val)

        # If there are more elements in the array, add the next one to the heap
        if element_index + 1 < len(arrays[array_index]):
            next_element = arrays[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, array_index, element_index + 1))

    return result

# Example usage
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
result = merge_k_sorted_arrays([array1, array2, array3])
print(result)