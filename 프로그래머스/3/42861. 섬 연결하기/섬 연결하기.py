def solution(n, costs):
    answer = 0
    reps = [i for i in range(n)]
    costs.sort(key=lambda x: x[-1])
    for fr, to, cost in costs:
        if not is_same_set(reps, fr, to):
            union_set(reps, fr, to)
            answer += cost
    return answer

def union_set(reps, a, b):
    reps[find_rep(reps, b)] = find_rep(reps, a)

def is_same_set(reps, a, b):
    return find_rep(reps, a) == find_rep(reps, b)
    
def find_rep(reps, x):
    if reps[x] == x:
        return x
    reps[x] = find_rep(reps, reps[x])
    return reps[x]