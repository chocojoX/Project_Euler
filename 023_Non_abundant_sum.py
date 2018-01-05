import numpy as np
import math
from bisect import *

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def sum_of_divisors(n):
    divisors = divisorGenerator(n)
    return np.sum(list(divisors)[:-1])


def is_abundant(n):
    return sum_of_divisors(n)>n


def all_abundants_up_to(n):
    abundants = []
    for i in range(n):
        if is_abundant(i):
            abundants.append(i)
    return abundants


def is_sum_of_two(numbers_list, n):
    for a in numbers_list:
        if (n-a) in numbers_list:
            return True
    else:
        return False


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1
    raise ValueError

def run():
    n=28123
    all_abundants = all_abundants_up_to(n)
    not_sum_of_two = [i for i in range(n)]
    for (i, a) in enumerate(all_abundants):
        for (j, b) in enumerate(all_abundants[i:]):
            idx = index(not_sum_of_two, a+b)
            if idx>-1:
                not_sum_of_two.pop(idx)
            # if a+b in not_sum_of_two:
            #     not_sum_of_two.remove(a+b)
            if a+b>n:
                break
    return np.sum(not_sum_of_two)


if __name__=="__main__":
    print(run())



if __name__=="__main__":
    print(is_abundant(12))
