def jump(nums):
    if len(nums) == 1:
        return 0
    jumps = 0
    current_end = 0
    current_farthest = 0

    for i in range(len(nums) - 1):
        current_farthest = max(current_farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = current_farthest  
    return jumps


nums = [2,3,1,1,4]
print(jump(nums))

