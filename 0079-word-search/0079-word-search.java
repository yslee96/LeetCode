class Solution {
    private static int m, n;
    private static final int[] dx = {0,1,0,-1}, dy= {1,0,-1,0};
    public boolean exist(char[][] board, String word) {
        m = board.length;
        n = board[0].length;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                    if(exist(i, j, word, 0, board)) return true;
            }
        }
        return false;
    }
    private boolean exist(int r, int c, String targetWord, int idx, char[][] board){
        
        if(idx>=targetWord.length()) 
            return true;

        if(r< 0 || r>=m || c<0 || c>=n || board[r][c]!=targetWord.charAt(idx))
            return false;

        boolean result;
        board[r][c] = '#';
        for(int i=0; i<4; i++){
            if(exist(r+dx[i], c+dy[i], targetWord, idx+1, board)) return true;
        }
        board[r][c] = targetWord.charAt(idx);
        return false;
    } 
}