class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[],[]]
        players = set()
        lose_num = defaultdict(int)
        for match in matches:
            winner, loser = match
            players.add(winner)
            lose_num[match[0]]+=0
            lose_num[match[1]]+=1
        results = sorted(lose_num.items())
        for result in results:
            if result[1] == 0:
                answer[0].append(result[0])
            elif result[1] == 1:
                answer[1].append(result[0])
        return answer
                    