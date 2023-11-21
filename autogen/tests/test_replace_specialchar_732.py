import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text = text().filter(lambda x: any(c in [' ', ',', '.'] for c in x))

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def replace_specialchar(text):
 return (re.sub("[ ,.]", ":", text))


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, replace_specialchar, *args)
