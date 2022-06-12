#!/usr/bin/env python3.9
import dis
from io import StringIO
from itertools import zip_longest

from uncompyle6.main import load_module
from z3 import Int, Solver

# from itertools docs
def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
	"Collect data into non-overlapping fixed-length chunks or blocks"
	# grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
	# grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
	# grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
	args = [iter(iterable)] * n
	if incomplete == 'fill':
		return zip_longest(*args, fillvalue=fillvalue)
	if incomplete == 'strict':
		return zip(*args, strict=True)
	if incomplete == 'ignore':
		return zip(*args)
	else:
		raise ValueError('Expected fill, strict, or ignore')

# from uncompyle6.main.decompile_file
code_objects = {}
(version, timestamp, magic_int, co, is_pypy, source_size,
	sip_hash) = load_module("eunectes-murinus.pyc", code_objects)

o = StringIO()
dis.dis(co, file=o)
asm = o.getvalue().splitlines()

vals = [line[line.rfind("(") + 1:-1] for line in asm[77:3275] if line.endswith(")")]

flag = [Int(f"x{i}") for i in range(58)]
solver = Solver()
for char in flag:
	solver.add(char > 0)
	solver.add(char < 128)

for tup in grouper(vals, 16):
	x0, x1, x2 = [int(x[1:]) for x in (tup[0], tup[2], tup[4])]
	y0, y1, y2 = [int(y) for y in (tup[7], tup[9], tup[11])]
	target = int(tup[12])
	solver.add((flag[x0] * y0) * (flag[x1] - y1) * (flag[x2] + y2) == target)

print(solver.check())
#print(solver.model())
m = solver.model()
s = "".join(chr(m[var].as_long()) for var in flag)
print(s)
with open("flag.txt") as f:
	print(s == f.read().strip())
