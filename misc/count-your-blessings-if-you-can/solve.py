def calc(n):
    mp.dps=int(n*0.8)
    beta = lambda k: mp.fdiv(1,mp.findroot(lambda x: 1-2*x+x**(k+1), 0.5))
    c = lambda p: mp.fdiv(functools.reduce(lambda a, b: mp.fadd(a,b), [mp.power(beta(p),(i+1)) for i in range(p)]),functools.reduce(lambda a, b: mp.fadd(a,b), [mp.fmul(p-i,mp.power(beta(p),i)) for i in range(p)]))
    return(str(int(ceil(mp.log(mp.fdiv(0.5,c(n)),b=mp.fdiv(beta(n),2))))))  
