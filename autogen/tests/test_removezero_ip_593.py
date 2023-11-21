import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def ip_address(draw):
    a = draw(integers(min_value=0, max_value=255))
    b = draw(integers(min_value=0, max_value=255))
    c = draw(integers(min_value=0, max_value=255))
    d = draw(integers(min_value=0, max_value=255))
    return f"{a}.{b}.{c}.{d}"

ip = ip_address()

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
