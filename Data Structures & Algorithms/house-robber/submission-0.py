class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}
        
        def raid(i):
            # Base case: we reached the end of the neighborhood
            if i >= len(nums): 
                return 0
                
            # If we've already calculated this step, return the saved answer
            if i in store:
                return store[i]
                
            # Choice 1: Rob this house and move 2 steps forward
            rob_current = nums[i] + raid(i + 2)
            
            # Choice 2: Skip this house and move 1 step forward
            skip_current = raid(i + 1)
            
            # Save the best choice in our memoization dictionary
            store[i] = max(rob_current, skip_current)
            return store[i]
            
        return raid(0)
        
