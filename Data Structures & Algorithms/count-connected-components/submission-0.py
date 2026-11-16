class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        seen = set()

        graph = {i: set() for i in range(n)}

        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)

        def dfs(node):
            if node in seen:
                return False

            seen.add(node)

            for nei in graph[node]:
                dfs(nei)

            return True
        
        res = 0 

        for i in range(n):
            if dfs(i):
                res += 1
        
        return res