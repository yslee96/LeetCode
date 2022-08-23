class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chs = {}
        for i in range(201):
            chs[i] = {}
        for string in strs:
            for i, ch in enumerate(string):
                if ch in chs[i]:
                    chs[i][ch] +=1
                else:
                    chs[i][ch] = 1
        total = len(strs)
        lcp = []
        for i in range(201):
            if len(chs[i]) == 1:
                tmp = list(chs[i].items())
                if tmp[0][1] == total:
                    lcp.append(tmp[0][0])
            else:
                break
        return "".join(lcp)