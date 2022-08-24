class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0 : return False
        while True:
            if n == 1:
                return True
            if n//3 > 0 and n% 3 == 0:
                n = n//3
            else:
                return False
            
            