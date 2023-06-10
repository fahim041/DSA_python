'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''


def permute(arr):
    result = []

    def backtrack(a):
        if len(a) == len(arr):
            result.append(a[:])
            return
        else:
            for i in arr:
                if i not in a:
                    a.append(i)
                    backtrack(a)
                    a.pop()
    backtrack([])
    return result


print(permute([1, 2, 3]))
