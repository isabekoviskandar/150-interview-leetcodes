def removeDuplicates(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    index = 0  
    for num in nums:
        if count[num] <= 2:  
            nums[index] = num
            index += 1

    for i in range(index, len(nums)):
        nums[i] = '_'

    return index

nums = [1, 1, 1, 2, 2, 3]
length = removeDuplicates(nums)


print("Output length:", length)
print("Modified nums:", nums[:length])  
print("Full nums array:", nums)         
