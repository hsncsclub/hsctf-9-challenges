#!/usr/bin/env python3.9
from uncompyle6.main import load_module
import dis

code_objects = {}
(version, timestamp, magic_int, co, is_pypy, source_size,
	sip_hash) = load_module("chall.pyc", code_objects)
dis.dis(co)
