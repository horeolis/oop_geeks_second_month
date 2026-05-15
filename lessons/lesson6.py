nums = [2,7,11,15]
target = 9

for i in range(len(nums)-1):
    print("проход номер", i)
    if nums[i] + nums[i+1] == target:
        print("[", i, ", ", i+1, "]")
        break
    else:
        print("No match")



