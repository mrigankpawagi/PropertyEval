import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text

word = text(alphabet='abcdeABCDE ').filter(lambda s: s.isalpha() or s == '')

strategy = word
