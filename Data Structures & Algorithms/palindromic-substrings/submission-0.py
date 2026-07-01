class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] will be True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        res = 0
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = True
            res += 1
            
        # Check substrings of length 2 to n
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                
                # A substring is a palindrome if the outer characters match 
                # AND the inner substring is also a palindrome
                if s[i] == s[j]:
                    # j - i <= 2 handles length 2 and 3 substrings without out-of-bounds errors
                    if j - i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1
                        
        return res