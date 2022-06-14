from pwn import *
import time
r = process(["python3","bucephala-albeola-the-second.py"])

def genBytes(index,length):
    s = "1"+"0"*index+"1"+"0"*(length-index-1)
    return(int(s, 2).to_bytes(-(-len(s) // 8), byteorder='big'))
    
def sendLine(b):
    r.recvuntil(": ")
    r.sendline(b)
    return(bin(int(r.recvline().decode().strip(),16))[2:])

a = []
for i in range(438):
    a.append(sendLine(genBytes(i,438)))
print(a)
