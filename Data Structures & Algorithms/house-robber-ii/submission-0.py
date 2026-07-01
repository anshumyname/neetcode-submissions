class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: If there is only one house, just rob it
        if len(nums) == 1:
            return nums[0]

        # Helper function for standard House Robber (Linear)
        def raid(houses, i, store):
            # Base case: we reached the end of the neighborhood
            if i >= len(houses):
                return 0
                
            # If we've already calculated this step, return the saved answer
            if i in store:
                return store[i]
                
            # Choice 1: Rob this house and move 2 steps forward
            rob_current = houses[i] + raid(houses, i + 2, store)
            
            # Choice 2: Skip this house and move 1 step forward
            skip_current = raid(houses, i + 1, store)
            
            # Save the best choice in our memoization dictionary
            store[i] = max(rob_current, skip_current)
            return store[i]
            
        # Scenario 1: Exclude the last house (nums[:-1])
        ans1 = raid(nums[:-1], 0, {})
        
        # Scenario 2: Exclude the first house (nums[1:])
        ans2 = raid(nums[1:], 0, {})
        
        # Return the maximum profit of the two valid scenarios
        return max(ans1, ans2)
        
        
