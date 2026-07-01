class Solution:
    def numDecodings(self, s: str) -> int:
        # dp dictionary maps an index 'i' to the number of valid decode ways.
        # Base case: reaching the end of the string counts as 1 valid way.
        dp = {len(s): 1}

        def count(i):
            # If we've already solved for this index, return the cached result
            if i in dp:
                return dp[i]
            
            # A valid decoding can NEVER start with a "0"
            if s[i] == "0":
                return 0

            # Branch 1: Decode a single character
            res = count(i + 1)

            # Branch 2: Decode two characters
            # We can only do this if we aren't at the last character, 
            # and the two characters form a valid number between 10 and 26.
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += count(i + 2)

            # Cache the result and return it
            dp[i] = res
            return res

        return count(0)