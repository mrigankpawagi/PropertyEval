import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
# Groundtruth seems wrong because problem only stated "every opening bracket has a corresponding closing bracket" and not vice versa. (More like an ambiguity)

from hypothesis.strategies import text

brackets = text(alphabet="<>")

strategy = brackets
