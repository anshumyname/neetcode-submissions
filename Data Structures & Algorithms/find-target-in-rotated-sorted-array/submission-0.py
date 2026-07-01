class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # Did we find it?
            if nums[mid] == target:
                return mid
                
            # Step 1: Is the LEFT half perfectly sorted?
            if nums[l] <= nums[mid]:
                # Step 2: Is our target within this sorted left half?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 # Yes, search left
                else:
                    l = mid + 1 # No, it must be on the right
                    
            # Step 1 (Alternate): The RIGHT half must be perfectly sorted!
            else:
                # Step 2: Is our target within this sorted right half?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # Yes, search right
                else:
                    r = mid - 1 # No, it must be on the left
                    
        return -1