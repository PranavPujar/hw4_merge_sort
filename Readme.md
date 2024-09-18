# HW4 -- Algorithm Problems -- Implementation and Analysis

# Fibonacci Sequence Implementation

## Code Implementation:
```python
def fib(n):

    if n == 0: return 0
    elif n == 1: return 1

    return fib(n-1) + fib(n-2)

x = fib(5)
print(x)

```


## Recursive Function Breakdown for `fib(5)`

To walk through the Fibonacci sequence as described, let's "step into" the function for `fib(5)` and trace each recursive call without optimization (like memoization). The function calls will follow the structure:

```
fib(5) -> fib(4) + fib(3)
        -> (fib(3) + fib(2)) + (fib(2) + fib(1))
        -> ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + 1)
        -> (((fib(1) + fib(0)) + 1) + (1 + 0)) + ((1 + 0) + 1)
        -> (((1 + 0) + 1) + (1 + 0)) + ((1 + 0) + 1)
        -> 5
```

Each recursive breakdown is like this:

1. `fib(5)` calls `fib(4)` and `fib(3)`
2. `fib(4)` calls `fib(3)` and `fib(2)`
3. `fib(3)` calls `fib(2)` and `fib(1)`
4. `fib(2)` calls `fib(1)` and `fib(0)`
5. Base cases: `fib(1) = 1` and `fib(0) = 0`

### Full Call Stack for `fib(5)`

The resulting call stack for `fib(5)` is as follows:

- fib(5)
  - fib(4)
    - fib(3)
      - fib(2)
        - fib(1) -> 1
        - fib(0) -> 0
      - fib(1) -> 1
    - fib(2)
      - fib(1) -> 1
      - fib(0) -> 0
  - fib(3)
    - fib(2)
      - fib(1) -> 1
      - fib(0) -> 0
    - fib(1) -> 1

This results in a value of `5` for `fib(5)`.

## Time Complexity

The time complexity of the recursive Fibonacci implementation without optimization is **O(2^n)** because each call results in two more recursive calls. There is a significant amount of redundant computation, making it inefficient for large values of `n`.

## Possible Improvements

- **Memoization**: Cache previously computed Fibonacci numbers to avoid redundant calculations. This reduces the time complexity to **O(n)**.
- **Bottom-up dynamic programming**: Iteratively compute the Fibonacci numbers from `0` to `n`, also leading to **O(n)** time complexity with **O(1)** space if only storing the last two values.

## Conclusion

This problem illustrates the inefficiency of simple recursive solutions to the Fibonacci sequence and highlights potential improvements through dynamic programming.

## Problem 1: Merging K Sorted Arrays

### Implementation

```python
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
```

### Time Complexity Proof

The time complexity of this algorithm is O(N _ K _ log(K)), where N is the average length of each array and K is the number of arrays.

Proof:

1. Initialization: Creating the min heap with the first element from each array takes O(K \* log(K)) time.
2. Main loop: We process N \* K elements in total (as there are K arrays with an average length of N).
   - For each element, we perform a heappop and potentially a heappush operation.
   - Both heappop and heappush take O(log(K)) time, as the heap size is at most K.
3. Therefore, the total time complexity is O(K _ log(K) + N _ K _ log(K)) = O(N _ K \* log(K)).

### Potential Improvements

1. Parallel processing: If the arrays are very large, we could partition the work across multiple threads or processors.
2. External sorting: For extremely large datasets that don't fit in memory, we could implement an external merge sort algorithm.
3. Use of more efficient data structures: In some cases, a self-balancing binary search tree might be more efficient than a heap, especially if we need to support operations like "find kth smallest element" efficiently.

## Problem 2: Removing Duplicates from a Sorted Array

### Implementation

```python
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
```

### Time Complexity Proof

The time complexity of this algorithm is O(N), where N is the length of the input array.

Proof:

1. We iterate through the array exactly once, from the second element to the last.
2. For each element, we perform a constant-time comparison and potentially a constant-time append operation.
3. Therefore, the total number of operations is directly proportional to the size of the input array.
4. This results in a linear time complexity of O(N).

### Potential Improvements

1. In-place removal: Instead of creating a new list, we could remove duplicates in-place to save space. This would be especially useful for very large arrays.
2. Handling unsorted arrays: The current implementation assumes the input array is sorted. We could modify it to handle unsorted arrays by using a set or dictionary to track unique elements.
3. Parallel processing: For extremely large arrays, we could partition the array and process different sections in parallel, then merge the results.
