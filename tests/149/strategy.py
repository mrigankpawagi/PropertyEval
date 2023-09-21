from hypothesis.strategies import text, lists
from functools import cmp_to_key

def cmp(s: str, t: str):
    if len(s) != len(t):
        return len(s) - len(t)
    return -1 if s < t else 1

lst = lists(text(alphabet="abcdef", max_size=10), max_size=15).map(lambda lst: sorted(lst, key=cmp_to_key(cmp)))

strategy = lst
