class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        nums = []
        for digit in x:
            nums.append(digit)
        return nums == nums[::-1]