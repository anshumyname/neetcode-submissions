class Solution:
    store = {}
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        if self.store.get(n, -1) != - 1: return self.store[n]
        self.store[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.store[n]