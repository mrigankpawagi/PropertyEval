import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text, integers

s = text(alphabet='abcdeABCDE ')
n = integers(min_value=0)

strategy = s, n
