class Solution:
    def subsets(self, nums):
        result = []
        stack = []

        def backtrack(i):
            if i >= len(nums):
                result.append(stack[:])
                return

            stack.append(nums[i])
            backtrack(i+1)

            stack.pop()
            backtrack(i+1)

        backtrack(0)
        return result
