import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text

s = text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())

strategy = s

# This inherently has a roundabout property-based test
