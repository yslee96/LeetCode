import sys
input = sys.stdin.readline

num_vertices = int(input())
graph = [list(map(int,input().split())) for _ in range(num_vertices)]

for k in range(num_vertices):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for i in range(num_vertices):
    print(*graph[i])