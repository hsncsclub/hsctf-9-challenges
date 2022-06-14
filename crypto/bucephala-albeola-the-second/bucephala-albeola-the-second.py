import random
import hashlib
import binascii
from Crypto.Util.number import *
try:
    flag = open('flag.txt','rb').read()
    pt = bytes_to_long(flag)
    p = 92097773344986149948746087607785504923724784346751915262381859825029576214181
    q = 67609158272666599806055762455573282890372265662234157788576501112025823079353
    n = p*q 
    def enc(a):
        return pow(a,65537,n)   
    def hash(a):
        m = hashlib.sha512()
        m.update(a.encode())
        return int.from_bytes(m.digest(), "big")
    while 1:
        plaintext = input("Input: ")
        binary = bin(int(binascii.hexlify(plaintext.encode('utf-8','surrogateescape')),16))[2:]
        l = len(binary)
        hashout = hash(str(enc(l*37+1)))
        for bit in range(l):
            if binary[bit]=="1":
                random.seed(enc((bit+21)*(l+37)+20))
                mask = int("".join(["1" if random.random()<0.5 else "0" for i in range(512)]),2)
                hashout^=mask
        print(hex(hashout)[2:])
except ValueError as err:
    print(err)
    print("woooo you threw an error. congratulations.")