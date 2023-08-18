class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def recursion(displayed, copied):
            print(displayed, copied)
            if (displayed, copied) in memo:
                return memo[(displayed, copied)]

            if displayed == n:
                return 0
            
            if displayed > n:
                return float('inf')

            copy_and_paste = recursion(displayed+displayed, displayed) + 2
            only_paste = float('inf')
            if copied:
                only_paste = recursion(displayed + copied, copied) + 1

            memo[(displayed, copied)] = min(copy_and_paste, only_paste)
            return memo[(displayed, copied)]
        return recursion(1,0)
         
            