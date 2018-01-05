import numpy as np
from utils.long_int import *

def factorial(n):
    if n==1:
        return LongInt(1)
    else:
        x = factorial(n-1)
        x.multiply(n)
        return x


def run(n=100):
    return np.sum(factorial(n).number)


if __name__=="__main__":
    n=100
    print(run(n))
