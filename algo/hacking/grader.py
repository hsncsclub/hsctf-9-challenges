from random import randint 
import threading
import os

answered = False

def check():
    global answered

    if not answered: 
        print("You took too long :(")
        os._exit(1)


threading.Timer(25,check).start()


def solve(con):
    con = [x-1 for x in con]
    n = len(con)
    
    visited = [False]*n
    finalized = [False]*n
    cured = [False]*n
    
    def calc(count, k):
        if finalized[k]:
            return 0
        
        if cured[k]:
            return count
        
        cured[k] = True
        
        add = calc(count + 1, con[k])
        
        finalized[k] = True
        return add
        
    
    def dfs(k): 
        if visited[con[k]]:
            return calc(0, k)

        visited[k] = True
        return dfs(con[k])
        
    ans = 0
    for k in range(n): 
        if not visited[k]: 
            ans += dfs(k)
    
    return ans 

sizes = map(int, [10, 300, 1e5, 1e6, 1e6])
test_cases = [[randint(1, n) for k in range(n)] for n in sizes]

print("Input:")
for case in test_cases: 
    print(", ".join(map(str, case)))


response = input().split(", ")
answered = True 

print("Deliberating your response...")
    
if list(map(int, response)) == [solve(case) for case in test_cases]: 
    print(r"flag{cOnGrAtS_yOu_ArE_nOw_A_hAcKeR}")
else: 
    print("Boohoo you messed up :(")
os._exit(1)