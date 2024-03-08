import sys
from collections import deque

input = sys.stdin.readline

test_cases = int(input())
for _ in range(test_cases):
    cmds = input().rstrip()
    arr_size = int(input())
    arr = input().rstrip()[1:-1].split(",")
    deq = deque(arr)

    if arr_size == 0:
        deq = deque()
    reverse_cnt = 0
    is_error = False

    for cmd in cmds:
        if cmd == "R":
            reverse_cnt += 1
        else:
            if len(deq) == 0:
                is_error = True
                break
            else:
                if reverse_cnt % 2:
                    deq.pop()
                else:
                    deq.popleft()

    if reverse_cnt % 2:
        deq.reverse()

    print("error" if is_error else "[" + ",".join(deq) + "]")
