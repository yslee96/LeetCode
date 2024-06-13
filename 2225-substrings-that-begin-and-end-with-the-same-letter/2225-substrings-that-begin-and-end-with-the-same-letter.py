class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum(map(lambda x: (x*(x+1)) // 2, Counter(s).values()))
        