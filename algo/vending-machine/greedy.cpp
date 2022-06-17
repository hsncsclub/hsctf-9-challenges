#include <bits/stdc++.h>

using namespace std;

void disp(int n){
	for(int i = 0; n; i ++){
		if(n % 2) cout << i + 1 << " ";
		n /= 2;
	}
	cout << endl;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n;
	cin >> n;
	vector<int> items(n);
	for(int i = 0; i < n; i ++){
		string s;
		cin >> s >> items[i];
	}
	int m;
	cin >> m;
	vector<int> coins(m);
	for(int i = 0; i < m; i ++){
		string s;
		cin >> s >> coins[i];
	}

	int k = 1 << m;
	vector<int> sum(k);
	for(int i = 0; i < k; i ++){
		for(int j = 0; j < m; j ++){
			if(i & (1<<j)){
				sum[i] += coins[j];
			}
		}
	}

	int used = 0;
	for(int i = 0; i < n; i ++){
		int best = INT_MAX;
		int mask = 0;
		for(int j = 0; j < k; j ++){
			if(used & j) continue;
			if(sum[j] > items[i] && sum[j] < best){
				best = sum[j];
				mask = j;
			}
		}
		used |= mask;
		disp(mask);
	}
	
	return 0;
}

