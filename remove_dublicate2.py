def removeDuplicates(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    index = 0  # Pointer for the in-place modification
    for num in nums:
        if count[num] <= 2:  # Keep numbers that appear 2 or fewer times
            nums[index] = num
            index += 1

    # Fill the rest of the array with placeholder values (optional)
    for i in range(index, len(nums)):
        nums[i] = '_'

    return index

nums = [1, 1, 1, 2, 2, 3]
length = removeDuplicates(nums)

# Output the result
print("Output length:", length)
print("Modified nums:", nums[:length])  # Print only the valid part of nums
print("Full nums array:", nums)         # Print the entire nums array with placeholders
