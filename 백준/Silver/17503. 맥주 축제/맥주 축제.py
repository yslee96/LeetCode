import sys
input = sys.stdin.readline
days, favors, drinks = map(int, input().split())
beers = []
min_alch = float('inf')
max_alch = 0
for _ in range(drinks):
    v, c = map(int, input().split())
    max_alch = max(c, max_alch)
    min_alch = min(c, min_alch)
    beers.append((v,c))
beers.sort(key= lambda x: -x[0])
start, end = min_alch, max_alch
answer = float('inf')
def check(mid):
    tmpFavor = 0
    beerCnt = 0
    for i in range(drinks):
        if beerCnt == days:
            break
        if beers[i][1] <= mid:
            tmpFavor += beers[i][0]
            beerCnt +=1
    if beerCnt!=days or tmpFavor < favors:
        return False
    return True

while start <= end:
    mid = start + (end-start)//2
    if check(mid):
        end = mid-1
        answer = min(answer, mid)
    else:
        start = mid+1
print(-1) if answer == float('inf') else print(answer) 