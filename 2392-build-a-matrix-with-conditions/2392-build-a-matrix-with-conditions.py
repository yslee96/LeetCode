class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rows = []
        inDegree1 = [0 for _ in range(k+1)]
        graph1 = [ [] for _ in range(k+1)]
        queue1 = deque()
        for i in range(len(rowConditions)):
            a, b = rowConditions[i]
            graph1[a].append(b)
            inDegree1[b] +=1
        for i in range(1, k+1):
            if inDegree1[i] == 0:
                queue1.append(i)
        while queue1:
            tmp = queue1.popleft()
            rows.append(tmp)
            for i in graph1[tmp]:
                inDegree1[i] -=1
                if inDegree1[i] == 0:
                    queue1.append(i)
        cols = []
        inDegree2 = [0 for _ in range(k+1)]
        graph2 = [ [] for _ in range(k+1)]
        queue2 = deque()
        for i in range(len(colConditions)):
            a, b = colConditions[i]
            graph2[a].append(b)
            inDegree2[b]+=1
        for i in range(1, k+1):
            if inDegree2[i] == 0:
                queue2.append(i)
        while queue2:
            tmp = queue2.popleft()
            cols.append(tmp)
            for i in graph2[tmp]:
                inDegree2[i]-=1
                if inDegree2[i] == 0:
                    queue2.append(i)

        if len(rows) < k or len(cols) < k:
            return []
        
        locs = [[] for _ in range(k+1)]
        for i, num in enumerate(rows):
            locs[num].append(i)
        for i, num in enumerate(cols):
            locs[num].append(i)
 
        locs = locs[1:]
        result = [[0 for _ in range(k)] for _ in range(k)]
        for i, loc in enumerate(locs):
            result[loc[0]][loc[1]] = i+1
        
        return result
