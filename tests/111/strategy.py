from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text, builds

def space_out(s: str):
    return " ".join(s)

test = builds(space_out, text(alphabet="abcde", min_size=1, max_size=MAX_SEQUENCE_LEN))

strategy = test
