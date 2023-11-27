from limits.limits import *
# Error in CONTRACTs: Does not check that cnt == 0 at end!

from hypothesis.strategies import just, lists, recursive
from hypothesis import given

def paren_helper():
    base = just(' ') | just('')
    return recursive(base, lists)

def to_paren(s):
    s = ''.join(str(x) for x in s)
    s = s.replace('[', '(').replace(']', ')').replace(',', '').replace("'", '')
    return s

def paren_string():
    return paren_helper().map(to_paren)

strategy = paren_string()
