class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0 for _ in range(n+1)]
        for i in range(n+1):
            result[i] = result[i//2] + i%2
        return result
        