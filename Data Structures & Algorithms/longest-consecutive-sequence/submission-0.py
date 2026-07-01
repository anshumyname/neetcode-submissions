class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # Check if this is the START of a sequence
            if (n - 1) not in numSet:
                length = 1
                
                # Count consecutive numbers upwards
                while (n + length) in numSet:
                    length += 1
                    
                # Update our max length
                longest = max(longest, length)
                
        return longest
        