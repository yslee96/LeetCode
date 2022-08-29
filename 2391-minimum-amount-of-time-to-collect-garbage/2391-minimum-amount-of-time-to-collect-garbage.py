class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        collect_time = 0
        move_idx = [ 0, 0, 0]
        g_dict = {'M': 0, 'P':1, 'G':2}
        num_homes = len(garbage)
        num_garbage = [[0,0,0] for _ in range(num_homes)]
        for i, g in enumerate(garbage):
            collect_time += len(g)
            for ch in g:
                num_garbage[i][g_dict[ch]] +=1
        print(num_garbage)
        for i, g in enumerate(garbage):
            for j in range(3):
                if num_garbage[i][j] >0:
                    move_idx[j] = i
        print(move_idx)
        move_time = 0
        for i in range(3):
            move_time += sum(travel[:move_idx[i]])
        return collect_time + move_time
        
                