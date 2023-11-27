from limits.limits import *
from hypothesis.strategies import text
import re

sentence = text(alphabet="a ", min_size=1, max_size=100).map(lambda s: re.sub(r"\s+", " ", s)).filter(lambda s: not (s.startswith(" ") or s.endswith(" ")))

strategy = sentence
