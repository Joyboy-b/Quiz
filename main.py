def rob(nums):
    # If there are no houses, return 0
    if not nums:
        return 0
    
    # If there is only one house, rob it
    if len(nums) == 1:
        return nums[0]
    
    # Create a dp array to store the best total up to each house
    dp = [0] * len(nums)
    
    # Base cases
    dp[0] = nums[0]                       # Best you can do for the first house
    dp[1] = max(nums[0], nums[1])         # Best between first and second house
    
    # Fill the dp array for the rest of the houses
    for i in range(2, len(nums)):
        # Either skip the current house or rob it and add to dp[i-2]
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    # The last element has the maximum amount that can be robbed
    return dp[-1]



nums = [2, 7, 9, 3, 1]
print(rob(nums))  
