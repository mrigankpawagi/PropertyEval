from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, sampled_from

S = lists(sampled_from(['I ', ' '] + list('abcdefgh.?!')), max_size=MAX_SEQUENCE_LEN).map(''.join)

strategy = S
