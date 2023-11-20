import sys
from collections import defaultdict, deque
input = sys.stdin.readline
visitied = []
cmds = ['D', 'S', 'L', 'R']

def convert_num(cur_num, cmd):
    if cmd == 0:
        cur_num = 2 * cur_num % 10000        
    elif cmd == 1:
        cur_num = 9999 if cur_num == 0 else cur_num-1 
    elif cmd == 2:
        cur_num = str(cur_num).zfill(4)
        cur_num = cur_num[1:] + cur_num[0]
        cur_num = int(cur_num)
    else:
        cur_num = str(cur_num).zfill(4)
        cur_num = cur_num[-1] + cur_num[0:-1]
        cur_num = int(cur_num)
    return cur_num

def bfs(num, goal):
    q = deque()
    q.append([num, ''])
    visitied[num] = 1
    while q:
        cur_num, cur_cmds = q.popleft()
        
        if cur_num == goal:
            return cur_cmds
        
        for i in range(4):
            nxt_num = convert_num(cur_num, i)
            if visitied[nxt_num]: continue
            q.append([nxt_num, cur_cmds + cmds[i]])
            visitied[nxt_num] = 1

test_cases = int(input())
for _ in range(test_cases):
    visitied = defaultdict(int)
    init, goal = map(int, input().split())
    result_cmd = bfs(init, goal)
    print(result_cmd)