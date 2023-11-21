import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(alphabet=characters(whitelist_categories=('Lu', 'Ll')), min_size=1, max_size=100)

strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_uppercase(str1):
  return re.sub('[A-Z]', '', str1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_uppercase, *args)
