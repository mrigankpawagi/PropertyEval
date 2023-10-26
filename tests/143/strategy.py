from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text
import re

sentence = text(alphabet="a ", min_size=1, max_size=100).map(lambda s: re.sub(r"\s+", " ", s)).filter(lambda s: not (s.startswith(" ") or s.endswith(" ")))

strategy = sentence
