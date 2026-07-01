class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        seen = {}
        for i in range(N):
            if (target-nums[i]) in seen.keys():
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i
        return []
        