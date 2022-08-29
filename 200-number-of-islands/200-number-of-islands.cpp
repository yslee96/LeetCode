class Solution {
public:
    int dx[4] = {0,1,0,-1};
    int dy[4] = {1,0,-1,0};
    int isVisited[301][301];
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int islandCnt = 0;
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(!isVisited[i][j] && grid[i][j]=='1'){
                    islandCnt++;
                    queue<pair<int, int> > bfsQueue;
                    bfsQueue.push({i,j});
                    isVisited[i][j] = 1;
                    while(!bfsQueue.empty()){
                        int curRow = bfsQueue.front().first;
                        int curCol = bfsQueue.front().second;
                        bfsQueue.pop();
                        for(int i=0; i<4; i++){
                            int newRow = curRow + dx[i];
                            int newCol = curCol + dy[i];
                            if(newRow < 0 || newRow >=rows || newCol < 0 || newCol>=cols) continue;
                            if(isVisited[newRow][newCol]) continue;
                            if(grid[newRow][newCol]=='1'){
                                bfsQueue.push({newRow, newCol});
                                isVisited[newRow][newCol] = 1;
                            }
                        }
                    }
                }
            }
        }
        return islandCnt;
    }
};