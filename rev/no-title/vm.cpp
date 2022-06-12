#include <array>
#include <climits>
#include <cstdint>
#include <deque>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

/*const std::vector<std::string> debug = {"mov",	"jump", "load", "store", "const", "add",
										"sub",	"xor",	"and",	"or",	 "push",  "pop",
										"call", "ret",	"getc", "putc"};*/
const std::array<uint16_t, 128> instructions = {
	26756, 14980, 28548, 30084, 27012, 26756, 14980, 24708, 25220, 24964, 27524, 20868, 26756,
	25220, 14212, 28548, 29572, 16260, 27012, 15492, 20868, 28548, 16004, 27524, 14468, 15236,
	1028,  4,	  2948,	 1924,	2820,  3204,  1412,	 2564,	3076,  2436,  1284,	 1156,	2180,
	516,   1540,  2692,	 1668,	772,   1796,  388,	 132,	2052,  644,	  260,	 2308,	900,
	9217,  644,	  651,	 45575, 37381, 61957, 13,	 3332,	267,   128,	  17797, 3458,	3586,
	1666,  5507,  4227,	 58501, 17798, 8001,  13,	 3332,	139,   132,	  907,	 14,	58502,
	9761,  7564,  128,	 19205, 1538,  6796,  2948,	 651,	45575, 61957, 50821, 5762,	45575,
	1316,  4260,  13220, 14116, 14244, 14628, 11172, 47,	47,	   47,	  47,	 47,	47,
	47,	   45,	  58501, 17798, 1300,  4244,  14868, 12692, 12948, 14612, 14612, 14228, 8596,
	31,	   31,	  31,	 31,	31,	   31,	  31,	 31,	31,	   29,	  10497};
std::deque<int> stack{};
std::vector<uint16_t> ret_addrs{};
std::array<int, 8> registers{};
bool zero_flag = false;
bool sign_flag = false;

void two_arg(uint8_t ins, uint16_t encoded) {
	int& dest = registers.at(encoded & 0b111);
	encoded >>= 3;
	int& src = registers.at(encoded & 0b111);
	encoded >>= 3;
	switch (ins) {
		case 0:	 // mov
			dest = src;
			break;
		case 2:	 // load
			dest = stack[src];
			break;
		case 3:	 // store
			stack[dest] = src;
			break;
		default:
			throw std::runtime_error(std::to_string(ins));
	}
}
void three_arg(uint8_t ins, uint16_t encoded) {
	// TODO set flags
	int& dest = registers.at(encoded & 0b111);
	encoded >>= 3;
	int& arg1 = registers.at(encoded & 0b111);
	encoded >>= 3;
	int& arg2 = registers.at(encoded & 0b111);

	switch (ins) {
		case 5:	 // add
			dest = arg1 + arg2;
			break;
		case 6:	 // sub
			dest = arg1 - arg2;
			break;
		case 7:	 // xor
			dest = arg1 ^ arg2;
			break;
		case 8:	 // and
			dest = arg1 & arg2;
			break;
		case 9:	 // or
			dest = arg1 | arg2;
			break;
		default:
			throw std::runtime_error(std::to_string(ins));
	}
	zero_flag = dest == 0;
	sign_flag = dest >= 0;
}

int main() {
	for (size_t ip = 0; ip < instructions.size(); ip++) {
		uint16_t encoded = instructions.at(ip);
		uint8_t ins = encoded & 0b1111;
		encoded >>= 4;
		uint8_t cond = encoded & 0b111;
		encoded >>= 3;

		// std::cout << debug.at(ins) << " " << std::to_string(cond) << "\n";

		bool should_run = false;
		switch (cond) {
			case 0:	 // NOP
				should_run = true;
				break;
			case 1:	 // z
				should_run = zero_flag;
				break;
			case 2:	 // nz
				should_run = !zero_flag;
				break;
			case 3:	 // g
				should_run = sign_flag && !zero_flag;
				break;
			case 4:	 // l
				should_run = !sign_flag && !zero_flag;
				break;
			case 5:	 // ge
				should_run = sign_flag || zero_flag;
				break;
			case 6:	 // le
				should_run = !sign_flag || zero_flag;
				break;
			default:
				throw std::runtime_error(std::to_string(cond));
		}
		if (!should_run) {
			continue;
		}

		switch (ins) {
			case 0:	 // mov
			case 2:	 // load
			case 3:	 // store
				two_arg(ins, encoded);
				break;
			case 5:	 // add
			case 6:	 // sub
			case 7:	 // xor
			case 8:	 // and
			case 9:	 // or
				three_arg(ins, encoded);
				break;
			case 1:				   // jump
				ip = encoded - 1;  // take into account ip++
				break;
			case 4:	 // const
			{
				// std::cout << std::to_string(encoded) << "\n";
				int val = encoded;
				stack.push_front(val);
				break;
			}
			case 10:  // push
			{
				int& src = registers.at(encoded & 0b111);
				stack.push_front(src);
				break;
			}
			case 11:  // pop
			{
				int& dest = registers.at(encoded & 0b111);
				dest = stack.front();
				stack.pop_front();
				break;
			}
			case 12:  // call
				ret_addrs.push_back(ip + 1);
				ip = encoded - 1;  // take into account ip++
				break;

			case 13:  // ret
				if (ret_addrs.empty()) {
					ip = INT_MAX - 1;  // take into account ip++
				} else {
					ip = ret_addrs.back() - 1;	// take into account ip++
					ret_addrs.pop_back();
				}
				break;
			case 14:  // getc
			{
				int c = std::cin.get();
				stack.push_front(c);
				break;
			}
			case 15:  // putc
			{
				char i = stack.front();
				stack.pop_front();
				std::cout << i;
				break;
			}
			default:
				throw std::runtime_error(std::to_string(ins));
		}
	}
	/*for (auto i : stack) {
		std::cout << std::to_string(i) << ' ';
	}*/
}