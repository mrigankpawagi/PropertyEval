from limits.limits import *
from hypothesis.strategies import text, lists
from functools import cmp_to_key

def cmp(s: str, t: str):
    if len(s) != len(t):
        return len(s) - len(t)
    return -1 if s < t else 1

lst = lists(text(alphabet="abcdef", max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN).map(lambda lst: sorted(lst, key=cmp_to_key(cmp)))

strategy = lst
