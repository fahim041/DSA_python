def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = high - 1
    return -1


a = [2, 4, 6, 7, 8, 11, 55]
print(binary_search(a, 6))
