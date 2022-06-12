#!/usr/bin/env python3.10
from z3 import Solver, Int
import random

with open("flag.txt") as f:
	flag = f.read().strip()
flag_chars = flag.encode()
solver = Solver()
variables = [Int(f"x{i}") for i in range(len(flag))]
var_names = [
	"kurnakovite", "akimotoite", "pyrophanite", "aerinite", "fayalite", "clinohumite", "allanite",
	"chalcocite", "covellite", "halloysite"
]

code = [",".join(f"x{i}" for i in range(len(flag))) + " = input('flag?\\n').encode()"]

for var in variables:
	solver.add(var > 0)
	solver.add(var < 128)

for _ in range(120):
	x0, x1, x2 = [random.randrange(0, len(flag)) for _ in range(3)]
	v0, v1, v2 = random.sample(var_names, k=3)
	code.append(f"({v0}:=x{x0},{v1}:=x{x1},{v2}:=x{x2})")
	
	y0, y1, y2 = [random.randrange(1, 10) for _ in range(3)]
	target = (flag_chars[x0] * y0) * (flag_chars[x1] - y1) * (flag_chars[x2] + y2)
	solver.add((variables[x0] * y0) * (variables[x1] - y1) * (variables[x2] + y2) == target)
	
	code.append(
		f"if ({v0}*{y0}) * ({v1} - {y1}) * ({v2} + {y2}) != {target}:return print('Failed')"
	)

code.append("return print('Success')")

print(solver.check())
#print(solver.model())
m = solver.model()

s = "".join(chr(m[var].as_long()) for var in variables)
print(s)
print(s == flag)
if s != flag:
	exit(1)

with open("chall.py", "w") as f:
	f.write("def fun():\n\t" + "\n\t".join(code))
	f.write("\nfun()")