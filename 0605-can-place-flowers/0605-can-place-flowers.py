class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = max(0, i - 1)
                right = min(len(flowerbed), i+1)
                if sum(flowerbed[left:right+1]) == 0:
                    flowerbed[i] = 1
                    n-=1
        return True if n <= 0 else False

