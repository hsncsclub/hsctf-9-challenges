#include <bits/stdc++.h>

using namespace std;

const int N = 8;

double score(vector<int> v){
	vector<double> p;
	p.assign(N, ((double) 1)/N);
	for(int x : v){
		p[x] = 0;
		vector<double> next(N);
		for(int i = 1; i < N - 1; i ++){
			next[i + 1] += p[i] / 2;
			next[i - 1] += p[i] / 2;
		}
		next[1] += p[0];
		next[N-2] += p[N-1];
		p = next;
	}
	double res = 0;
	for(double k : p) res += k;
	return res;
}

set<pair<double, vector<int> > > s;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	vector<int> test = {4, 2, 5, 2, 2, 6, 5, 6};
	vector<int> test1 = {3, 1, 4, 1, 1, 5, 4, 5};
	cout << score(test) << " " << score(test1) << endl;
	return 0;

	vector<int> v;
	double best = 1;
	for(int i = 0; i < pow(N, N); i ++){
		vector<int> k(N);
		int t = i;
		for(int j = 0; j < N; j ++){
			k[j] = t % N;
			t /= N;
		}
		double test = score(k);
		if(test < best){
			cout << best << endl;
			best = test;
			v = k;
		}
	}
	for(int x : v) cout << x << " ";
	cout << endl;
	cout << 1 - best << endl;

	return 0;
}

