def twoSum(nums, target):
    hashMap = {}

    for i, v in enumerate(nums):
        diff = target - v

        if diff in hashMap:
            return [hashMap[diff], i]

        hashMap[v] = i
