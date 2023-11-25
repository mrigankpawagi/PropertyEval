import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
ip = text(alphabet=characters(min_codepoint=48, max_codepoint=57), min_size=7, max_size=15).filter(lambda s: '.' in s and all(int(num) >= 0 and int(num) <= 255 for num in s.split('.')))
strategy = ip
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def removezero_ip(ip):
 string = re.sub('\.[0]*', '.', ip)
 return string


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, removezero_ip, *args)
