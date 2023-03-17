def combine(n, k):
    stack = []
    res = []

    def backtrack(remain, next):
        if remain == 0:
            res.append(stack[:])
            return
        else:
            for i in range(next, len(n) + 1):
                stack.append(i)
                backtrack(remain-1, i+1)
                stack.pop()

    backtrack(k, 1)
    return res


print(combine([1, 2, 3, 4], 3))
