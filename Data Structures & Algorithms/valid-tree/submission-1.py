class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vis = [0]*n
        adj_list = [[] for i in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(c):
            vis[c] = 1
            for i in adj_list[c]:
                if not vis[i]:
                    dfs(i)
        
        dfs(0)
        N = len(edges)
        if not all(vis): return False
        return N == (n-1)
        