import sys
input = sys.stdin.readline
test_cases = int(input())
dp = []

def game(start, end, turn):
    if start > end:
        return 0
    
    if dp[start][end]:
        return dp[start][end]
    
    if turn % 2 == 0:
        dp[start][end] = min(game(start+1, end, turn+1), game(start, end-1, turn+1))
    else:
        dp[start][end] = max(cards[start] + game(start+1, end, turn+1), cards[end] + game(start, end-1, turn+1))
        
    return dp[start][end]

for _ in range(test_cases):
    num_cards = int(input())
    cards = list(map(int, input().split()))
    dp = [[0 for _ in range(num_cards)] for _ in range(num_cards)]
    game(0, num_cards-1, 1)
    print(dp[0][num_cards-1])
    