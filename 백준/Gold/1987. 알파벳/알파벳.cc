#include<iostream>
#include<algorithm>
#include<unordered_set>
using namespace std;
char board[21][21];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int maxRow, maxCol;
int alphabet[26];
int getMaxDist(int row, int col){
    int ret = 1;
    for(int i=0; i<4; i++){
        int nRow, nCol;
        nRow = row + dx[i];
        nCol = col + dy[i];
        if(nRow<0 || nRow>=maxRow || nCol<0 || nCol>=maxCol) continue;
        if(alphabet[(int)board[nRow][nCol]-65]==1) continue;
        alphabet[(int)board[nRow][nCol]-65]=1;
        ret = max(ret, 1 + getMaxDist(nRow, nCol));
        alphabet[(int)board[nRow][nCol]-65]=0;
    }
    return ret;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie();
    cin >> maxRow >> maxCol;
    for(int i=0; i<maxRow; i++){
        for(int j=0; j<maxCol; j++){
            cin >> board[i][j];
        }
    }
    alphabet[(int)board[0][0]-65]=1;
    cout << getMaxDist(0,0) <<"\n";
    return 0;
}