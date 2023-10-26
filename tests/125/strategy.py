import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text

txt = text(alphabet='abcdeFGHIJ,. \n\t\r').filter(lambda s: not s.startswith(" ") and not s.startswith(",") and not s.endswith(" ") and not s.endswith(","))

strategy = txt
