#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

// dP + 가장 긴 증가 부분수열

int main()
{
    int num;
    int max = 1;
    int dp[101];
    int seq[101];
    vector<pair<int, int> > line;
    cin >> num;

    for (int i = 0; i < num; i++)
    {
        dp[i] = 1;
        int a, b;
        cin >> a >> b;
        line.push_back(make_pair(a, b));
    }

    sort(line.begin(), line.end()); // 왼쪽오름차순

    for (int i = 0; i < num; i++)
    { // 오른쪽만 저장
        seq[i] = line[i].second;
    }

    for (int i = 1; i < num; i++) // 가장 긴 증가하는 부분수열
    {
        for (int j = 0; j < i; j++)
        {
            if (seq[i] > seq[j] && dp[i] < dp[j] + 1)
            {
                dp[i] = dp[j] + 1;
            }
        }
        if (max < dp[i])
        {
            max = dp[i];
        }
    }

    cout << num - max << endl;
    return 0;
}