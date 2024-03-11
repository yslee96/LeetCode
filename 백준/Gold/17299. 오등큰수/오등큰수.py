import sys
from collections import Counter
input = sys.stdin.readline
num_size = int(input())
stack = list(map(int, input().split()))
counts = Counter(stack)
results = [0 for _ in range(num_size)]

indices = [0]
for i in range(1, num_size):
    if not indices:
        indices.push_back(i)
    else:
        while indices and counts[stack[indices[-1]]] < counts[stack[i]]:
            results[indices[-1]] = stack[i]
            indices.pop()
        indices.append(i)

for result in results:
    print(result if result !=0 else -1, end=" ")
