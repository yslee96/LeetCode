#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstring>
using namespace std;
int map[10][10];
int isVisited[10][10];
vector<pair<int, int> > possiblePos, virusPos;
int maxRow, maxCol;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int maxCnt;

void setWallsAndBFS(vector<pair<int,int> > walls){
    int tmpMap[10][10];
    for(int i=0; i<maxRow; i++){
        for(int j=0; j<maxCol; j++){
            tmpMap[i][j] = map[i][j];
        }
    }

    for(auto wall:walls)
        tmpMap[wall.first][wall.second] = 1;
    
    memset(isVisited, 0, sizeof(isVisited));
    int areaCnt = 0;
    for(auto virus: virusPos){
        queue<pair<int,int> > bfsQueue;
        bfsQueue.push({virus.first, virus.second});
        isVisited[virus.first][virus.second] = 1;
        while(!bfsQueue.empty()){
            auto curPos = bfsQueue.front();
            bfsQueue.pop();
            for(int i=0; i<4; i++){
                int newRow, newCol;
                newRow = curPos.first + dx[i];
                newCol = curPos.second + dy[i];
                if(newRow <0 || newRow>=maxRow || newCol<0 || newCol>=maxCol) continue;
                if(isVisited[newRow][newCol]) continue;
                isVisited[newRow][newCol] = 1;
                if(tmpMap[newRow][newCol]==0){
                    tmpMap[newRow][newCol]= 2;
                    bfsQueue.push({newRow, newCol});
                }
            }
        }
    }

    for(int i=0; i<maxRow; i++){
        for(int j=0; j<maxCol; j++){
            if(tmpMap[i][j]==0)
                areaCnt++;
        }
    }
    maxCnt = max(maxCnt, areaCnt);
}
int main(void){
    ios_base::sync_with_stdio(0); cin.tie(0);
    cin >> maxRow >> maxCol;
    for(int i=0; i<maxRow; i++){
        for(int j=0; j<maxCol; j++){
            cin >> map[i][j];
            if(map[i][j]==0)
                possiblePos.push_back({i,j});
            else if(map[i][j]==2)
                virusPos.push_back({i,j});
        }
    }
    // 벽 세울 위치 고르기 - 브루트포스
    for(int i=0; i<possiblePos.size()-2; i++){
        for(int j=i+1; j<possiblePos.size()-1; j++){
            for(int k=j+1; k<possiblePos.size(); k++){
                vector<pair<int,int>> walls;
                walls.push_back(possiblePos[i]);
                walls.push_back(possiblePos[j]);
                walls.push_back(possiblePos[k]);
                setWallsAndBFS(walls);
            }
        }
    }
    cout << maxCnt <<"\n";
    return 0;       
}