from collections import Counter
def solution(participant, completion):
    participant_info, completion_info = Counter(participant), Counter(completion)
    return [name for name in set(participant) if participant_info[name] != completion_info[name] ][0]
    