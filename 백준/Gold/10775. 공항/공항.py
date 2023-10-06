import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
num_gates = int(input())
num_planes = int(input())
gates_to_dock = [int(input()) for _ in range(num_planes)]
reps = [i for i in range(num_gates+1)]

def find_rep(num):
    if reps[num] == num:
        return num
    reps[num] = find_rep(reps[num])
    return reps[num]

result = 0
for i in range(num_planes):
    # 게이트 대표 번호에 dock
    cur_rep_gate = find_rep(gates_to_dock[i])
    # 처음에는 자기 번호 == 대표번호
    if not cur_rep_gate: break
    result+=1
    # 도킹한 게이트의 대표번호(자기번호 이하)를 1씩 감소시키고 그 번호의 대표번호가 새로운 대표가됨
    reps[cur_rep_gate] = find_rep(cur_rep_gate-1)
print(result)
