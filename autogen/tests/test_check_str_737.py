import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
import re

def check_str(string): 
    """Write a function to check whether the given string is starting with a vowel or not using regex.
    >>> check_str("annie")
    True
    >>> not check_str("dawood")
    True
    >>> check_str("Else")
    True
    """
    return re.search('^[aeiouAEIOU]', string) is not None

s = from_regex('^[aeiouAEIOU]', fullmatch=True)
strategy = s,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	return re.search(regex, string)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_str, *args)
