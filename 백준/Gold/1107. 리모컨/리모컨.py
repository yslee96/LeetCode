import sys
input = sys.stdin.readline
target = int(input())
num_brokens = int(input())
brokens = list(map(int, input().split())) if num_brokens else []
is_broken = [False for _ in range(10)]
for broken in brokens:
    is_broken[broken] = True
    
# 초기값: +/- 버튼만 사용해서 100에서 target 까지 가는 count
min_count = abs(100 - target)

# 숫자버튼 눌러서 특정 번호에서 시작해 타겟까지의 카운트 계산
# 타겟 번호가 최대 500,000 이므로 999,999 이상은 체크할 필요 x
for channel_num in range(1000000):
    channel_num = str(channel_num)
    for idx in range(len(channel_num)):
        if is_broken[int(channel_num[idx])]:
            break
        if idx == len(channel_num) - 1:
            min_count = min(min_count, abs(int(channel_num) - target) + len(channel_num))
print(min_count)