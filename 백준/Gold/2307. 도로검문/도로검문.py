import sys
from heapq import heappop, heappush
input = sys.stdin.readline

num_vertices, num_edges = map(int, input().split())
graph = [[] for _ in range(num_vertices+1)]
paths = [-1 for _ in range(num_vertices+1)]

def dijkstra(a, b, is_first):
    dists = [float('inf') for _ in range(num_vertices+1)]
    pq = []
    heappush(pq, [0, 1])
    dists[1] = 0
    
    while pq:
        cur_dist, cur_vertex = heappop(pq)
        if dists[cur_vertex] < cur_dist:
            continue
        for nxt_vertex, next_dist in graph[cur_vertex]:
            if (not is_first) and ((a,b)==(cur_vertex, nxt_vertex) or (a,b)==(nxt_vertex,cur_vertex)): continue
            if dists[nxt_vertex] > cur_dist+next_dist:
                if is_first:
                    paths[nxt_vertex] = cur_vertex
                heappush(pq, [cur_dist+next_dist, nxt_vertex])
                dists[nxt_vertex] = cur_dist+ next_dist
    
    return dists[num_vertices]


for _ in range(num_edges):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2,cost))
    graph[v2].append((v1,cost))

orgin_exit_time = dijkstra(-1,-1, True)
cur_vertex = num_vertices
max_delay = 0

while paths[cur_vertex] != -1:
    a, b = cur_vertex, paths[cur_vertex]
    max_delay = max(max_delay, dijkstra(a,b,False) - orgin_exit_time)
    if max_delay == float('inf'):
        break
    cur_vertex = paths[cur_vertex]
max_delay = -1 if max_delay == float('inf') else max_delay
print(max_delay)