class Solution {
public:
    int visited[100001];
    vector<int> path[100001];
    int possibleNodes;
    void dfs(int curNode){
        if(visited[curNode]) 
            return;
        visited[curNode] = 1;
        possibleNodes++;
        for(int nextNode : path[curNode])
            dfs(nextNode);
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
        dfs(0);
        return possibleNodes;
    }
};