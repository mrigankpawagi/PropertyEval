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
                
string = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=1)
string_with_repeated_char = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=2, max_size=MAX_SEQUENCE_LEN).flatmap(
    lambda s: builds(lambda x: x + s[0], s[1:])
)
string_without_repeated_char = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=2, max_size=MAX_SEQUENCE_LEN).map(
    lambda s: s[0] + s[1:].replace(s[0], '')
)

valid_string = one_of(string, string_with_repeated_char)
invalid_string = string_without_repeated_char

string_strategy = valid_string | invalid_string

strategy = string_strategy,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
def check_char(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "Invalid" 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_char, *args)
