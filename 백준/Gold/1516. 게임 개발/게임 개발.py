import sys
input = sys.stdin.readline
from collections import deque

num_types = int(input())
build_infos = [[] for _ in  range(num_types+1)]

in_degree = [0 for _ in range(num_types+1)]
queue = deque()
build_times = [0 for _ in range(num_types+1)]
build_costs = [0 for _ in range(num_types+1)]

for i in range(1, num_types+1):
    build_info = list(map(int, input().split()))
    build_times[i] = build_info[0]
    build_costs[i] = build_info[0]
    for num in build_info[1:-1]:
        build_infos[num].append(i)
        in_degree[i] += 1
        
for i in range(1, num_types+1):
    if in_degree[i] == 0:
        queue.append(i)
        
while queue:
    tmp = queue.popleft()
    for num in build_infos[tmp]:
        in_degree[num] -= 1
        build_costs[num] = max(build_costs[num], build_costs[tmp] + build_times[num])
        if in_degree[num] == 0:
            queue.append(num)

print(*build_costs[1:], sep='\n')
