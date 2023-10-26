import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import dictionaries, text, one_of, integers

_dict = dictionaries(one_of(integers(min_value=0, max_value=MAX_INT), text(alphabet='aA0', min_size=1, max_size=MAX_SEQUENCE_LEN)), text(alphabet='aA0', max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)

strategy = _dict
