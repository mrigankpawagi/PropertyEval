import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
string = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1)
strategy = string
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
def test_fuzz(args):
    run_with_timeout(0.3, check_char, *args)
