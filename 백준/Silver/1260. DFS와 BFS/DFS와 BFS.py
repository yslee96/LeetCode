import sys
from collections import defaultdict, deque
input = sys.stdin.readline
dfs_visited = defaultdict(int)
bfs_visited = defaultdict(int)
dfs_result, bfs_result = [], []

def dfs(vertex, edges):
    global dfs_result
    dfs_result.append(vertex)
    dfs_visited[vertex] = 1
    for nxt_vertex in edges[vertex]:
        if dfs_visited[nxt_vertex]: continue
        dfs(nxt_vertex, edges)

def bfs(vertex, edges):
    global bfs_result
    
    q = deque()
    q.append(vertex)
    bfs_visited[vertex] = 1
    
    while q:
        cur_vertex = q.popleft()
        bfs_result.append(cur_vertex)
        for nxt_vertex in edges[cur_vertex]:
            if bfs_visited[nxt_vertex]: continue
            q.append(nxt_vertex)
            bfs_visited[nxt_vertex] = 1


num_vertices, num_edges, start_vertex = map(int, input().split())
edges = [[] for _ in range(num_vertices+1)]
for _ in range(num_edges):
    fr, to = map(int, input().split())
    edges[fr].append(to)
    edges[to].append(fr)
    
for edge in edges:
    edge.sort()
    
dfs(start_vertex, edges)
bfs(start_vertex, edges)

print(*dfs_result)
print(*bfs_result)