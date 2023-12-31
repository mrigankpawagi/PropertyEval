import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import string
str1 = text(alphabet=string.ascii_letters + ' ', min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, capital_words_spaces, *args)
