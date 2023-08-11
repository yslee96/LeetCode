class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        connect_info = defaultdict(lambda: False)
        visited = [False for _ in range(n)]
        edges = [[] for _ in range(n)]
        for connect in connections:
            fr, to = connect
            edges[fr].append(to)
            edges[to].append(fr)
            connect_info[(fr,to)] = True

        ans = 0
        def dfs(num, toward_zero):
            ret = 0
            if visited[num]:
                return 0
            visited[num] = True

            if num > 0 and not toward_zero:
                ret+=1
            
            for nxt_num in edges[num]:
                ret += dfs(nxt_num, connect_info[(nxt_num, num)])            
            return ret

        return dfs(0, None)








