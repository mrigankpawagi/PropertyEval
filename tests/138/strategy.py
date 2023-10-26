from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
# CONTRACT is not exhaustive!

from hypothesis.strategies import integers

n = integers()

strategy = n
