class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')' : '(', '}':'{', ']':'['}
        for ch in s:
            if ch in pair.values():
                stack.append(ch)
            else:
                if stack and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        