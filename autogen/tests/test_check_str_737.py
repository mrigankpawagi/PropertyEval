import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import re

string = builds(lambda x, y: x + y, text(alphabet='aeiou', min_size=1, max_size=1), text(min_size=1, max_size=MAX_SEQUENCE_LEN))
vowel_regex = re.compile(r"^[aeiou]")

strategy = string.filter(lambda s: bool(vowel_regex.match(s)))
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	return re.search(regex, string)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_str, *args)
