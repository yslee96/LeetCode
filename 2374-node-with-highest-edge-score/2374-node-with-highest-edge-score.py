class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0 for _ in range(len(edges))]
        for i in range(len(edges)):
            scores[edges[i]] += i
        total = []
        for i in range(len(scores)):
            total.append((i,scores[i]))
        total.sort(key=lambda x: (-x[1],x[0]))
        return total[0][0]