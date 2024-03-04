#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int min(int a, int b);
int dp[1001][1001];
int main(void){
	int n, m, i, j,num, max=0;
	scanf("%d %d", &n, & m);
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= m; j++) {
			scanf("%1d", &num);
			if (num == 1) {
				if ((dp[i - 1][j - 1] != 0) && (dp[i - 1][j] != 0) && (dp[i][j - 1] != 0)) {
					dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1;
				}

				else
					dp[i][j] = 1;
			}
			else 
				dp[i][j] = 0;
	
			if (max < dp[i][j]) {
				max = dp[i][j];
			}
		}
	}
	printf("%d", max*max);
	return 0;
}


int min(int a, int b) {
	if (a < b)
		return a;
	return b;
}
