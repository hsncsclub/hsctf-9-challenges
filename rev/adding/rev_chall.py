def load(): 
    pass # Content not shown 

flag = load()

def func1(require = [], go = False):       
    if go: 
        require.append(20)
        return require
        
    add = func1(go = True)
    require += add
    return require 

add = 10 

def therealreal(update):
    def modify(require = []):
        require += update()
        
        global add 
        require.append(add)
        add += 10
        return require
    
    return modify
    
use = therealreal(func1)
upto = 64

calc = use()
for _ in range(1, upto+1):
    calc = use(calc)
    
if int(input("Enter the sum: ")) == sum(calc): 
    print(flag)
else: 
    print("Boohoo you didn't get it :(")
    print(sum(calc))