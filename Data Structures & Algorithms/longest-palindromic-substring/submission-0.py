class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i][j] will be True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        # Variables to track the longest palindrome found
        res_start = 0
        max_len = 1
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = True
            
        # Check substrings of length 2 to n
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                
                # If outer characters match...
                if s[i] == s[j]:
                    # It's a palindrome if it's length 2, OR the inner string is a palindrome
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        
                        # Update our longest tracking variables
                        if l > max_len:
                            max_len = l
                            res_start = i
                            
        return s[res_start : res_start + max_len]