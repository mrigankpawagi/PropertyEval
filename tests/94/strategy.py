from limits.limits import *
from hypothesis.strategies import lists, integers

def is_prime(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

lst = lists(integers(min_value=MIN_INT, max_value=MAX_INT)).filter(lambda l: any(is_prime(x) for x in l))

strategy = lst
