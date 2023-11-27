from limits.limits import *
from hypothesis.strategies import text, builds

def space_out(s: str):
    return " ".join(s)

test = builds(space_out, text(alphabet="abcde", min_size=1, max_size=MAX_SEQUENCE_LEN))

strategy = test
