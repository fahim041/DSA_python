# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeDuplicates(nums):
    l = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[l] = nums[i]
            l += 1
    return l