nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print('[',i,'][',j,']')
    return []

two_sum(nums, target)