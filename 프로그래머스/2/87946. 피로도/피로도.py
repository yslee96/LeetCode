from itertools import permutations
def solution(k, dungeons):
    answer = -1
    idx = [i for i in range(len(dungeons))]
    candidates = list(permutations(idx, len(dungeons)))
    for candidate in candidates:
        cur_fatigue = k
        dungeon_cnt = 0
        for idx in candidate:
            if cur_fatigue < dungeons[idx][0]:
                break
            else:
                dungeon_cnt+=1
                cur_fatigue -= dungeons[idx][1]
        answer = max(answer, dungeon_cnt)
        if answer == len(dungeons):
            return len(dungeons)
    return answer