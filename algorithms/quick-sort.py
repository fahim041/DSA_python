def quick(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot = arr.pop()

    greater = []
    smaller = []

    for i in arr:
        if pivot > i:
            smaller.append(i)
        else:
            greater.append(i)

    return quick(smaller) + [pivot] + quick(greater)


print(quick([5, 2, 5, 7, 12, 3, 6, 8, 2, 5, 7]))
