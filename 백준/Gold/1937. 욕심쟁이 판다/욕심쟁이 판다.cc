#include<iostream>
#include<algorithm>
using namespace std;

int board[501][501];
int dp[501][501];
int dx[4] = {0,-1,0,1};
int dy[4] = {1,0,-1,0};
int size;

int dfs(int row, int col){
    if(dp[row][col]>0){
        return dp[row][col];
    }

    int cnt = 1;
    for(int i=0; i<4; i++){
        int nRow = row + dx[i];
        int nCol = col + dy[i];
        if(nRow < 0 || nRow>=size||nCol<0 || nCol>=size) continue;
        if(board[nRow][nCol]> board[row][col]){
            cnt = max(cnt, 1 + dfs(nRow, nCol));
        }
    }

    return dp[row][col] = cnt;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> size;
    for(int i=0; i<size; i++){
        for(int j=0; j<size; j++){
            cin >> board[i][j];
        }
    }


    int ans = 0;
    for(int i=0; i<size; i++){
        for(int j=0; j<size; j++){
            ans = max(ans, dfs(i,j));
        }
    }

    cout << ans <<"\n";
    return 0;
}