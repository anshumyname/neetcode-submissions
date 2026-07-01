class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        
        # This keeps track of the frequency of the most abundant character 
        # in our current window.
        maxf = 0
        
        for r in range(len(s)):
            # 1. Add the new character to our window's frequency map
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # 2. Update our highest frequency count
            maxf = max(maxf, count[s[r]])
            
            # 3. The Validity Check: 
            # If the number of characters we need to replace is greater than k,
            # our window is invalid. Shrink it from the left.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            # 4. Now that the window is guaranteed to be valid, update our max result
            res = max(res, r - l + 1)
            
        return res