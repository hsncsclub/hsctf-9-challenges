#!/bin/bash
python3.9 gen_chall.py || exit
rm __pycache__/chall.cpython-39.pyc
python3.9 -m py_compile chall.py
cp __pycache__/chall.cpython-39.pyc eunectes-murinus.pyc
python3.9 eunectes-murinus.pyc < flag.txt
