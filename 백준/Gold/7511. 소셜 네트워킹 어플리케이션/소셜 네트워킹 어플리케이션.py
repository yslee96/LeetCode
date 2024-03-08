import sys

input = sys.stdin.readline
reps = []


def find_rep(num):
    if reps[num] == num:
        return num
    reps[num] = find_rep(reps[num])
    return reps[num]


def union_set(set1, set2):
    reps[find_rep(set2)] = find_rep(set1)


def is_same_set(set1, set2):
    return find_rep(set1) == find_rep(set2)


test_cases = int(input())
for test_case in range(1, test_cases + 1):
    num_users = int(input())
    reps = [i for i in range(num_users)]
    num_relations = int(input())
    for _ in range(num_relations):
        user_a, user_b = map(int, input().split())
        if not is_same_set(user_a, user_b):
            union_set(user_a, user_b)

    print(f"Scenario {test_case}:")

    num_pairs = int(input())
    for _ in range(num_pairs):
        u, v = map(int, input().split())
        print(1 if is_same_set(u, v) else 0)

    print()
