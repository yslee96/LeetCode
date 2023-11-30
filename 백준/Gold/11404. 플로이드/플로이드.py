import sys
input = sys.stdin.readline
num_cities = int(input())
num_buses = int(input())
costs = [[float('inf')] * (num_cities+1) for _ in range(num_cities+1)]
for _ in range(num_buses):
    a, b, cost = map(int, input().split())
    costs[a][b] =  min(costs[a][b], cost)

for k in range(1, num_cities+1):
    for i in range(1, num_cities+1):
        for j in range(1, num_cities+1):
            if i==j: continue
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

for i in range(1, num_cities+1):
    for j in range(1, num_cities+1):
        if costs[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(costs[i][j], end= ' ')
    print()