def quick(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot = arr.pop()

    greater = []
    smaller = []

    for i in arr:
        if pivot > i:
            greater.append(i)
        else:
            smaller.append(i)

    return quick(greater) + [pivot] + quick(smaller)


print(quick([5, 2, 5, 7, 12, 3, 6, 8, 2, 5, 7]))
