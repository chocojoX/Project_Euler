import numpy as np
import math


def get_nth_permutation_first(n, numbers_list):
    numbers_list = sorted(numbers_list)
    fact = math.factorial(len(numbers_list)-1)
    print(fact)
    k = int(n/fact)
    print(k)

    first = numbers_list.pop(k)
    return first, numbers_list, n-k*fact


def get_nth_permutation(n, numbers_list):
    permutation = []
    while len(numbers_list)>0:
        first, numbers_list, n = get_nth_permutation_first(n, numbers_list)
        permutation.append(first)
    return permutation


def run(n=1000000):
    numbers_list = [0,1,2,3,4,5,6,7,8,9]
    return get_nth_permutation(n-1, numbers_list)


if __name__=="__main__":
    print(run())
