def majorityElement(nums):
    count = {}
    length = len(nums)

    for num in nums:
        if num in count:
            count[num] +=1
        else:
            count[num] = 1

        if count[num] > length //2:
            return num
        
nums = [3,2,3]

print(majorityElement(nums))    