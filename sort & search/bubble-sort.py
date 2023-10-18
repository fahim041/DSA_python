def bubble(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr) - i - 1):
            if (arr[j + 1] < arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j + 1]
                swap = True
        if not swap:
            break
    return arr


print(bubble([5, 2, 5, 7, 2, 45, 7, 8, 9]))
