class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{', '[']
        pair = {')' : '(', '}':'{', ']':'['}
        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if stack and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        