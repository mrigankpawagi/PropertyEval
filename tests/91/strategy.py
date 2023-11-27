from limits.limits import *
from hypothesis.strategies import lists, sampled_from

S = lists(sampled_from(['I ', ' '] + list('abcdefgh.?!')), max_size=MAX_SEQUENCE_LEN).map(''.join)

strategy = S
