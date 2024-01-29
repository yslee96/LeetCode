#include<iostream>
#include<algorithm>
using namespace std;

int square[501][501];
int isVisited[501][501];
int isVisited2[501][501];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int n,m;
int maximum =0;
int except = 0;

void exc(int row, int col){
    
    int sum1=0;
    int sum2=0;
    int rest1 =0;
    int rest2 =0;
    int sum;
    for(int i=0; i<3; i++){
        if(row+i>=n) sum1 =-1;
        else sum1 += square[row+i][col];
        if(col+i>=m) sum2 = -1;
        else sum2 += square[row][col+i];
    }

    for(int i=0; i<4; i++){
        if(sum1>0 && i%2==0){
            if(row+1<0 || row+1>=n || col+dy[i]<0 || col+dy[i]>=m ) continue;
            rest1 = max(rest1, square[row+1][col+dy[i]]);
        }
        if(sum2>0 && i%2==1){
            if(row+dx[i]<0 || row+dx[i]>=n || col+1<0 || col+1>=m ) continue;
            rest2 = max(rest2, square[row+dx[i]][col+1]);
        }
    }
    
    sum = max(sum1+rest1, sum2+rest2);
    except = max(except, sum);

}

void tetromino(int row, int col, int sum, int k){
    
    sum += square[row][col];
    maximum = max(sum, maximum);

    if(k==3) return;

    for(int i=0; i<4; i++){
        if(row+dx[i]<0 || row+dx[i]>=n || col+dy[i]<0 || col+dy[i]>=m ) continue;
        if(isVisited[row+dx[i]][col+dy[i]]) continue;
        isVisited[row][col] =1;
        tetromino(row+dx[i], col+dy[i], sum, k+1);
        isVisited[row][col] = 0;
    }


    return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> square[i][j];
    
    
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++){
            tetromino(i,j,0,0);
            exc(i,j);
        }

    maximum = max(maximum, except);
    cout << maximum << "\n";
    return 0;
}