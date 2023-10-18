def quick(arr):
    def sort(arr, s, e):
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        arr[e] = arr[left]
        arr[left] = pivot

        sort(arr, s, left - 1)
        sort(arr, left + 1, e)

        return arr

    return sort(arr, 0, len(arr) - 1)


print(quick([5, 2, 5, 7, 12, 3, 6, 8, 2, 5, 7]))
