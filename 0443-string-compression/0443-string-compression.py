class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        res = 0
        while idx < len(chars):
            group_len = 1
            while idx + group_len < len(chars) and chars[idx+group_len] == chars[idx]:
                group_len+=1
            chars[res] = chars[idx]
            res +=1
            if group_len > 1:
                str_repeat = str(group_len)
                chars[res:res+len(str_repeat)] = list(str_repeat)
                res += len(str_repeat)
            idx += group_len 
        return res