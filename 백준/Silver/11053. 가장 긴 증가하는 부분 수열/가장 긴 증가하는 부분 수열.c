#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int seq[1001] = { 0, };
int dp[1001] = { 0, };
int main(void) {
	int N, i, j, max = 1;
	scanf("%d", &N);
	for (i = 1; i <= N; i++) {
		scanf("%d", &seq[i]);
		dp[i] = 1;
	}
	for (i = 2; i <= N; i++) {
		for (j = 1; j < i; j++) {
			if (seq[i] > seq[j] && dp[i] < dp[j]+1) {
				dp[i] = dp[j]+1;
			}
		}
		if (max < dp[i]) {
			max = dp[i];
		}
	}
	printf("%d\n", max);
	return 0;

}