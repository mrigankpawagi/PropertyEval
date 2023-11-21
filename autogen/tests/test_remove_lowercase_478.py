import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_string(draw):
    letters = draw(lists(text(alphabet=string.ascii_letters, min_size=1, max_size=1)))
    return ''.join(letters)

str1 = create_string()

strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_lowercase(str1):
 return re.sub('[a-z]', '', str1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_lowercase, *args)
