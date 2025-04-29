def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
