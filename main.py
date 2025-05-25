def pipe_fix(nums):
    nums.sort()
    return [i for i in range(nums[0], nums[-1] + 1)]

nums = [10,3,15,6,7,8]
print(pipe_fix(nums))
