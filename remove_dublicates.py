def removeDuplicates(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                nums.pop(j);
    return len(nums);

def remove(nums):
    uniques = []

    for i in range(len(nums)):
        if i not in nums:
            uniques.append(i)
    return len(uniques) 