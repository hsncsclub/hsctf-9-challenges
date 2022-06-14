"""
When you first open the file and try to simply run the program, you will quickly 
notice that it takes too long. Thus, we must understand what is happening to solve 
this challenge. Specifically, we want to understand how calc is modified and develop
a formula to calculate what the sum is. After some tracking you will notice that aside 
from the 20 gained from the global add, on the nth iteration we gain 2^(n+1) - 2 20s. 
The global add contributes n*10 on the nth iteration. You can either sum these in a loop
or simplify using formulas. The derivation for this problem (and hence the solve script too)
is shown below. 
"""

flag = "flag{tHiS_iS_oNe_FuN_cHaLlEnGe_NoW_iSnT_iT?}"

upto = 213
upto = upto + 1
ans = 10*(upto)*(upto+1)//2 + 20*(2**(upto+2) - 2*upto - 4)

if int(input("Enter the sum: ")) == ans: 
    print(flag)

else: 
    print("Boohoo you didn't get it :(")