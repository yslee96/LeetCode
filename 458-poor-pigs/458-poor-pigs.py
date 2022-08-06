class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        testNum = minutesToTest // minutesToDie
        numPigs = 0
        while (testNum+1)**numPigs < buckets:
            numPigs +=1
        return numPigs