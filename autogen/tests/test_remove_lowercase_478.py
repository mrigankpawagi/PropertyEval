import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(alphabet=string.ascii_lowercase + string.ascii_uppercase,
            min_size=SMALL_SEQUENCE_LEN,
            max_size=MAX_SEQUENCE_LEN)

strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_lowercase(str1):
 return re.sub('[a-z]', '', str1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_lowercase, *args)
