import time
import random
from mpmath import *
import functools
def calc(n):
    mp.dps=int(n*0.9)
    beta = lambda k: mp.fdiv(1,mp.findroot(lambda x: 1-2*x+x**(k+1), 0.5))
    c = lambda p: mp.fdiv(functools.reduce(lambda a, b: mp.fadd(a,b), [mp.power(beta(p),(i+1)) for i in range(p)]),functools.reduce(lambda a, b: mp.fadd(a,b), [mp.fmul(p-i,mp.power(beta(p),i)) for i in range(p)]))
    return(str(int(ceil(mp.log(mp.fdiv(0.5,c(n)),b=mp.fdiv(beta(n),2))))))  
#flag = open('/flag.txt','r').read().strip()
flag = "flag{thisisatempflag}"
print("Hello! Welcome to the challenge. To get the flag, answer the following question correctly:")
ans = input("Consider a fair coin, which lands heads and tails each with a 50% probability. What is the fewest number of times I must flip the coin in order be 50% sure that there are at least 4 consecutive heads in my flips?\n")
if ans!="22":
    print("Incorrect, sorry.")
    exit(0)
print("Correct! Here's the flag:")
time.sleep(3)
print("Wait, I just heard from the challenge writer that you have to answer another question.")
r = random.randint(15,30)
ans = input("Consider a fair coin, which lands heads and tails each with a 50% probability. What is the fewest number of times I must flip the coin in order be 50% sure that there are at least {} consecutive heads in my flips?\n".format(r))
if ans!=calc(r):
    print("Incorrect, sorry.")
    exit(0)
print("Correct! Here's the flag:")
time.sleep(3)
print("Wait, I just heard from the challenge writer that you have to answer yet another question. He promises it's the last one.")
r = random.randint(300,600)
ans = input("Consider a fair coin, which lands heads and tails each with a 50% probability. What is the fewest number of times I must flip the coin in order be 50% sure that there are at least {} consecutive heads in my flips?\n".format(r))
if ans!=calc(r):
    print("Incorrect, sorry.")
    exit(0)
print("Correct! Here's the flag:")
time.sleep(5)
print(flag)
