class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = set()
        i = 1 
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                factors.add(n//i)
            i+=1
        factors = sorted(list(factors))
        return factors[k-1] if len(factors) >=k else -1
