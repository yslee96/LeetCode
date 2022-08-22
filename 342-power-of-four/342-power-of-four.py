class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while True:
            if n % 4 == 0:
                n = n//4
            else:
                if n == 1:
                    return True
                else:
                    return False
                    
            