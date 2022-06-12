/* C++ implementation of the VM's code */
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
const std::vector<int> indicies = {7,  18, 2,  5,  16, 1,  3,  14, 6,  13, 21, 12, 4,
								   17, 9,  10, 19, 24, 20, 11, 25, 22, 15, 23, 0,  8};
const std::vector<int> match = {119, 113, 215, 125, 223, 163, 121, 211, 127, 231, 223, 111, 197,
								209, 163, 215, 195, 197, 193, 117, 209, 211, 235, 223, 117, 209};

int fun(std::uint8_t i) {
	return (i ^ 5) * 2 + 1;
}

void swap(std::vector<uint8_t>& l) {
	for (size_t i = 0; i < indicies.size(); i++) {
		uint8_t tmp = l[indicies[i]];
		l[indicies[i]] = l[i];
		l[i] = tmp;
	}
}

int main() {
	std::string s;
	std::cin >> s;
	std::vector<uint8_t> l(s.rbegin(), s.rend());
	size_t i = s.size() - 1;
	if (l.size() < 26) {
		std::cout << "Wrong!\n";
		return 1;
	}
	swap(l);
	/*for (auto i : l) {
		std::cout << std::to_string(i) << ' ';
	}*/
	for (int i = 0; i < 26; i++) {
		// std::cout << (fun(l.at(i)) ^ 23) + 1 << ", ";
		if (((fun(l.at(i)) ^ 23) + 1) != match.at(i)) {
			std::cout << "Wrong!\n";
			return 1;
		}
	}
	std::cout << "Correct!\n";
	return 0;
}
