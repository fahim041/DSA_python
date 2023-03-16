def combine(n, k):
    stack = []
    res = []

    def backtrack(remain, next):
        if remain == 0:
            res.append(stack[:])
            return
        else:
            for i in range(next, n + 1):
                stack.append(i)
                backtrack(remain-1, i+1)
                stack.pop()

    backtrack(k, 1)
    return res


print(combine(4, 3))
