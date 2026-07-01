class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P = 1
        pre = []
        for p in nums:
            pre.append(P)
            P*=p
        
        N = len(nums)
        ans = [1]*N
        S = 1
        for i in range(N-1, -1, -1):
            ans[i] = pre[i] * S 
            S *= nums[i]
        return ans