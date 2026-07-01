class Solution:
    def canFinish(self, N: int, prereq: List[List[int]]) -> bool:
        instack = set()
        adj_lis = [[] for i in range(N)]

        for a, b in prereq:
            adj_lis[a].append(b)
        
        def dfs(v):
            if v in instack: return False
            
            instack.add(v)

            for n in adj_lis[v]:
                if not dfs(n):
                    return False

            instack.remove(v)
            return True

        for i in range(N):
            if dfs(i)==False: return False
        
        return True

        