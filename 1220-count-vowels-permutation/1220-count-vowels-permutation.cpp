class Solution {
public:
    int mod = 1000000007;
    long long dp[20001][5];
    int countVowelPermutation(int n) {
        for(int i=0; i<5; i++)
            dp[1][i] = 1;
        for(int i=2; i<=n; i++){
            dp[i][0] += dp[i-1][1];
            dp[i][1] += (dp[i-1][0] + dp[i-1][2]);
            dp[i][2] += (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]);
            dp[i][3] += (dp[i-1][2] + dp[i-1][4]);
            dp[i][4] += dp[i-1][0];
            for(int j=0; j<5; j++)
                dp[i][j] %= mod;
        }
        int ans = 0;
        for(int i=0; i<5; i++){
            ans += dp[n][i];
            ans %= mod;
        }
        return ans;
    }
};