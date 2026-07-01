class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP table with a value greater than any possible answer (amount + 1)
        dp = [amount + 1] * (amount + 1)
        
        # Base case
        dp[0] = 0
        
        # Build the DP table bottom-up, from amount 1 up to the target amount
        for a in range(1, amount + 1):
            for c in coins:
                # If the current coin can be part of the solution
                if a - c >= 0:
                    # Take the minimum of what we already found, or 1 + the remainder
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # If dp[amount] is still our "infinity" value, it means it's impossible
        if dp[amount] == amount + 1:
            return -1
            
        return dp[amount]