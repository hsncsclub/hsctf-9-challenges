#include <bits/stdc++.h>

using namespace std;

void print_subset(int x, int N){
	for(int i = 0; i < N; i ++){
		if(x & (1 << i))
			cout << i + 1 << " ";
	}
	cout << endl;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int N, M;
	string s;
	cin >> N;
	vector<int> items(N);
	for(int i = 0; i < N; i ++) cin >> s >> items[i];
	cin >> M;
	vector<int> coins(M);
	for(int i = 0; i < M; i ++) cin >> s >> coins[i];

	int K = 1 << M;
	vector<int> sum(K); //sums of subsets of coins
	for(int i = 0; i < K; i ++){
		for(int j = 0; j < M; j ++){
			if(i & (1 << j)) sum[i] += coins[j];
		}
	}
	
	cout << K << " " << M << endl;
	vector<int> dp(K); //maximum number of items per subset of coins
	vector<int> parent(K);
	for(int i = 1; i < K; i ++){ //iterate of coin subsets
		for(int j = i; j > 0; j = (j - 1) & i){ //iteration over subsets of subset
			int k = i ^ j; //remaining coins
			if(dp[i] != N && sum[j] >= items[dp[k]]){
				if(dp[k] + 1 > dp[i]){
					dp[i] = dp[k] + 1;
					parent[i] = k;
				}
				if(dp[i] == N){
					while(i){
						print_subset(i ^ parent[i], M);
						i = parent[i];
					}
				}
			}
		}
	}
	
	return 0;
}

