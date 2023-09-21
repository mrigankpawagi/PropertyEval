from hypothesis.strategies import lists, integers

def is_prime(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

lst = lists(integers()).filter(lambda l: any(is_prime(x) for x in l))

strategy = lst
