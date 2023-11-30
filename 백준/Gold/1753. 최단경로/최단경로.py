import sys
from heapq import heappush, heappop
input = sys.stdin.readline
num_vertices, num_edges = map(int, input().split())
start_vertex = int(input())

graph = [[] for _ in range(num_vertices+1)]
dists = [-1 for _ in range(num_vertices+1)]

for _ in range(num_edges):
    fr, to, dist = map(int, input().split())
    graph[fr].append((to, dist))
    
pq = []
heappush(pq, [0, start_vertex])

while pq:
    cur_dist, cur_vertex = heappop(pq)
    if dists[cur_vertex]!=-1:
        continue
    dists[cur_vertex] = cur_dist
    
    for nxt_vertex, dist in graph[cur_vertex]:
        if dists[nxt_vertex] == -1:
            heappush(pq, [cur_dist+dist, nxt_vertex])
            
for i in range(1, num_vertices+1):
    if dists[i] == -1:
        dists[i] = 'INF'
    print(dists[i])