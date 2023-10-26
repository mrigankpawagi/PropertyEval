import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, text, recursive, just

def paren_helper():
    base = lists(text(), max_size=0)
    return recursive(base, lists)

def to_paren(s):
    s = ''.join(str(x) for x in s)
    s = s.replace(',', '').replace("'", '').replace(" ", "")
    return s

def paren_string():
    return paren_helper().map(to_paren)

string = paren_string()

strategy = string
