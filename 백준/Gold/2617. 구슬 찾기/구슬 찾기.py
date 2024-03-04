import sys

input = sys.stdin.readline
num_balls, num_pairs = map(int, input().split())
heavy_balls = [[] for _ in range(num_balls + 1)]
light_balls = [[] for _ in range(num_balls + 1)]

def dfs(balls, num):
    cnt = 0
    for ball in balls[num]:
        if not checked[ball]:
            checked[ball] = True
            cnt += 1
            cnt += dfs(balls, ball)

    return cnt

for _ in range(num_pairs):
    heavy, light = map(int, input().split())
    heavy_balls[light].append(heavy)
    light_balls[heavy].append(light)

result = 0

for i in range(1, num_balls + 1):
    checked = [False for _ in range(num_balls + 1)]
    if dfs(heavy_balls, i) >= (num_balls + 1) / 2:
        result += 1
    if dfs(light_balls, i) >= (num_balls + 1) / 2:
        result += 1

print(result)
