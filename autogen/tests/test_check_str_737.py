import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

def vowels():
    return st.sampled_from(['a', 'e', 'i', 'o', 'u'])

def check_str():
    return st.from_regex(r'^[aeiou]', fullmatch=True)

strategy = check_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	return re.search(regex, string)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_str, *args)
