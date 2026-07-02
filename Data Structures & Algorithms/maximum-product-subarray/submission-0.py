class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn = nums[0]
        maxn = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            
            # Store the candidates in temporary variables before overwriting minn/maxn
            temp_max = max(curr, maxn * curr, minn * curr)
            temp_min = min(curr, maxn * curr, minn * curr)
            
            # Update minn and maxn simultaneously
            maxn = temp_max
            minn = temp_min
            ans = max(ans, maxn)
        return ans