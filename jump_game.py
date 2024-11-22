def canJump(nums):
    max_reach = 0  # Keep track of the furthest position we can reach
    
    for i in range(len(nums)):
        # If we can't reach current position, return False
        if i > max_reach:
            return False
            
        # Update the furthest position we can reach from current position
        max_reach = max(max_reach, i + nums[i])
        
        # If we can already reach the last index, return True
        if max_reach >= len(nums) - 1:
            return True
    
    return True

# Test cases
test_cases = [
    [2,3,1,1,4],  # True
    [3,2,1,0,4],  # False
    [0],          # True
    [2,0],        # True
]

for nums in test_cases:
    print(f"Input: {nums}")
    print(f"Can reach end? {canJump(nums)}\n")
