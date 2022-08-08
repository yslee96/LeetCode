class Solution {
public:
    int visited[100001];
    vector<int> path[100001];
    int dfs(int curNode){
        int ret = 1;
        if(visited[curNode]) 
            return 0;
        visited[curNode] = 1;
        for(int nextNode : path[curNode])
            ret += dfs(nextNode);
        return ret;
    }
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        
        for(int i=0; i<restricted.size(); i++)
            visited[restricted[i]] = 1;
        for(int i=0; i<edges.size(); i++){
            int from, to;
            from = edges[i][0];
            to = edges[i][1];
            path[from].push_back(to);
            path[to].push_back(from);
        }
        return dfs(0);
    }
};