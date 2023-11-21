import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import re

vowels = ['a', 'e', 'i', 'o', 'u']
start_with_vowel = sampled_from(vowels)

def check_str():
    return strings().filter(lambda s: re.match(start_with_vowel, s[0]))

strategy = check_str()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	return re.search(regex, string)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_str, *args)
