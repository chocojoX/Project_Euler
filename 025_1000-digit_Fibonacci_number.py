import numpy as np
from utils.long_int import *
import copy

def fibo(n):
    if n==1:
        return (LongInt(1), LongInt(0))
    else:
        x = fibo(n-1)
        x[0].add_long(x[1])
        return x

def run(n_digits=1000):
    Fn = LongInt(1)
    F = LongInt(0)
    n = 1
    while len(Fn.number)<n_digits:
        n+=1
        foo = copy.deepcopy(Fn)
        Fn.add_long(F)
        F = foo
        print(n, len(Fn.number)) 
    return n


if __name__=="__main__":
    print(run())
