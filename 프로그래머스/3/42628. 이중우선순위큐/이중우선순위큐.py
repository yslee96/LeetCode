from collections import deque
from heapq import heapify

def solution(operations):
    pq = deque()
    for op in operations:
        cmd, num = list(op.split())
        if cmd == "I":
            pq.append(int(num))
        else:
            if not pq:
                continue
                
            pq = deque(sorted(list(pq)))
            if num == "1":
                pq.pop()
            elif num=="-1":
                pq.popleft()
                
    pq = sorted(list(pq))
    return [0,0] if not pq else [pq[-1], pq[0]]