def rotate(nums, k):
    k = k % len(nums)

    return nums[-k:] + nums[:-k]




nums = [-1,-100,3,99]
k = 2

print(rotate(nums,k))
#[5,6,7,1,2,3,4]
# 3-indexgacha bolgan sonlarni orqaga otqazish