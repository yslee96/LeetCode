import sys
input = sys.stdin.readline
from collections import deque

num_students, num_comparison = map(int, input().split())
edges = [[] for _ in range(num_students+1)]
for _ in range(num_comparison):
    shorter, taller = map(int, input().split())
    edges[shorter].append(taller)

confirms = [0 for _ in range(num_students+1)]
for student in range(1, num_students+1):
    q = deque()
    confirm_cnt = 0
    visited = [False for _ in range(num_students+1)]
    q.append(student)
    while q:
        student_num = q.popleft()
        if visited[student_num]: continue
        visited[student_num] = True
        confirm_cnt+=1
        confirms[student_num]+=1
        for taller in edges[student_num]:
            q.append(taller)
        
    confirms[student] += confirm_cnt-2

answer = 0
for i in range(1, num_students+1):
    if confirms[i] == num_students-1:
        answer +=1

print(answer)
    
