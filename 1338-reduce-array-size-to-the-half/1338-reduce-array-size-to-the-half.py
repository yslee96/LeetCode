class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        num_dict = {}
        total = len(arr)
        for num in arr:
            if num in num_dict:
                num_dict[num] +=1
            else:
                num_dict[num] = 1
        sorted_dict = list(num_dict.items())
        sorted_dict.sort(key= lambda x: -x[1])
        removed = 0
        cnt = 0
        for x in sorted_dict:
            removed += x[1]
            cnt +=1
            if removed >= total//2:
                break
        return cnt