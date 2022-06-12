#!/usr/bin/env python3
import re
import sys
import ast

# 4 bits for instruction, 3 bits for condition, 3 each for register arg
# -1 = varargs 3 = 3 registers -1 = 1 8-bit int
instructions = {
	"MOV": 2,  # mov reg to reg
	"JUMP": -1,  # unconditional
	"LOAD": 2,  # r = s[r]
	"STORE": 2,  # s[r] = r
	"CONST": -1,  # push const to stack
	"ADD": 3,  # dest, arg, arg
	"SUB": 3,
	"XOR": 3,
	"AND": 3,
	"OR": 3,
	"PUSH": 1,  # push r to stack
	"POP": 1,  # pop to r
	"CALL": -1,  # push return address to ret addr stack and jump
	"RET": 0,  # pop ret and jump
	"GETC": 0,  # push to stack
	"PUTC": 0
}
conditions = ["", "z", "nz", "g", "l", "ge", "le"]

encoded: list[int] = []
with open(sys.argv[1]) as f:
	lines = list(f)

# replace "ARRAY" and "PUTS" with instructions
to_insert = []

for i, line in enumerate(lines):
	# ignore comments and labels
	line = line.split("#")[0].split(":")[-1].strip()
	if not line:
		continue
	# this code sucks lol
	if line.split()[0].upper() == "ARRAY":
		instruction, _, cond = map(str.strip, line.partition("if"))
		vals = ast.literal_eval(line.split(maxsplit=1)[1])
		lines[i] = [f"CONST {val}" + cond for val in reversed(vals)]
	if line.split()[0].upper() == "PUTS":
		instruction, _, cond = map(str.strip, line.partition("if"))
		s = ast.literal_eval(instruction.split(maxsplit=1)[1])
		lines[i] = [f"CONST {ord(val)} if" + cond
			for val in reversed(s)] + ["PUTC if" + cond] * len(s)

lines = [line for line2 in lines for line in ([line2] if isinstance(line2, str) else line2)]

# define labels
line_no = 0
labels = {}

for line in lines:
	line = line.split("#")[0].strip()  # comments
	if not line:
		continue
	if ":" in line:
		label, _, line = map(str.strip, line.partition(":"))
		labels[label] = line_no
	line_no += 1

# encode instructions
for line in lines:
	# ignore comments and labels
	line = line.split("#")[0].split(":")[-1].strip()
	if not line:
		continue
	
	instruction, _, cond = map(str.strip, line.partition("if"))
	ins, *args = map(str.strip, instruction.split())
	ins = ins.upper()
	
	ins_encoded = list(instructions.keys()).index(ins)
	
	if cond == "e":
		cond = "z"
	if cond == "ne":
		cond = "nz"
	cond_encoded = conditions.index(cond)
	
	arg_format = instructions[ins]
	if arg_format > 0:  # registers
		if len(args) < arg_format:
			print(f"Not enough args for {line!r}, need {arg_format} args")
			sys.exit()
		
		args_encoded = []
		for arg in args:
			m = re.fullmatch(r"r(\d+)", arg)
			if not m:
				print(f"Invalid arg for {line!r}")
				sys.exit()
			args_encoded.append(int(m.group(1)))
		
		arg_encoded = ''.join(f'{arg:03b}' for arg in reversed(args_encoded)).zfill(9)
	elif arg_format == -1:  # 9-bit int
		arg = args[0]
		if ins in ("JUMP", "CALL") and not arg.isdigit():
			arg = labels[arg]
		arg_encoded = f"{int(arg):09b}"
	elif arg_format == 0:
		arg_encoded = "0" * 9
	
	encoded_ins = f"{arg_encoded}{cond_encoded:03b}{ins_encoded:04b}"
	#print(encoded_ins)
	encoded.append(int(encoded_ins, 2))

print(
	f"const std::array<uint16_t, {len(encoded)}> instructions = {{{', '.join(map(str,encoded))}}};"
)
