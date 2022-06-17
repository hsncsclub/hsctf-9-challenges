#include <bits/stdc++.h>

using namespace std;

int n = 56, m = 200;

pair<bool, vector<pair<int, vector<int> > > > check(vector<pair<int, int> > items, vector<int> coins){
	vector<bool> used(m);
	vector<pair<int, vector<int> > > sets;
	for(pair<int, int> itm : items){
		int x = itm.first;
		int best = INT_MAX;
		vector<int> pos;
		if(x < 120000){
			for(int i = 0; i < m; i ++){
				if(used[i]) continue;
				for(int j = i + 1; j < m; j ++){
					if(used[j]) continue;
					int test = coins[i] + coins[j];
					if(test >= x && test < best){
						best = test;
						pos = {i, j};
					}
				}
			}
			if(best == INT_MAX) return {false, sets};
			used[pos[0]] = used[pos[1]] = true;
		} else if(x < 160000){
			for(int i = 0; i < m; i ++){
				if(used[i]) continue;
				for(int j = i + 1; j < m; j ++){
					if(used[j]) continue;
					for(int k = j + 1; k < m; k ++){
						if(used[k]) continue;
						int test = coins[i] + coins[j] + coins[k];
						if(test >= x && test < best){
							best = test;
							pos = {i, j, k};
						}
					}
				}
			}
			if(best == INT_MAX) return {false, sets};
			used[pos[0]] = used[pos[1]] = used[pos[2]] = true;
		} else{
			for(int i = 0; i < m; i ++){
				if(used[i]) continue;
				for(int j = i + 1; j < m; j ++){
					if(used[j]) continue;
					for(int k = j + 1; k < m; k ++){
						if(used[k]) continue;
						for(int l = k + 1; l < m; l ++){
							if(used[l]) continue;
							int test = coins[i] + coins[j] + coins[k] + coins[l];
							if(test >= x && test < best){
								best = test;
								pos = {i, j, k, l};
							}
						}
					}
				}
			}
			if(best == INT_MAX) return {false, sets};
			used[pos[0]] = used[pos[1]] = used[pos[2]] = used[pos[3]] = true;
		}
		sets.push_back({itm.second, pos});
	}
	return {true, sets};
}

int main(){
	string s;
	cin >> s;
	vector<pair<int, int> > items(n);
	for(int i = 0; i < n; i ++){
		string s;
		cin >> s >> items[i].first;
		items[i].second = i + 1;
	}
	cin >> s;
	vector<int> coins(m);
	for(int i = 0; i < m; i ++){
		string s;
		cin >> s >> coins[i];
	}
	
	sort(items.begin(), items.end());
	vector<int> splits = {4, 16};
	pair<bool, vector<pair<int, vector<int> > > > q = check(items, coins);
	while(!q.first){
		cout << "retrying\n";
		random_shuffle(items.begin(), items.begin() + splits[0]);
		random_shuffle(items.begin() + splits[0], items.begin() + splits[1]);
		random_shuffle(items.begin() + splits[1], items.end());
		q = check(items, coins);
	}
	for(pair<int, vector<int> > p : q.second){
		cout << "Insert ";
		for(int x : p.second){
			cout << x + 1 << " ";
		}
		cout << endl;
		cout << "Buy " << p.first << endl;
	}
	
	return 0;
}

