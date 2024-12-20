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
                
l = lists(integers(), max_size=MAX_SEQUENCE_LEN)
s = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = l, s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, is_sublist, *args)
