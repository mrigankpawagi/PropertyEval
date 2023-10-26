from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import integers

def is_prime(a: int) -> bool:
        return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

n = integers(min_value=2, max_value=MAX_INT).filter(lambda x: not is_prime(x))

strategy = n
