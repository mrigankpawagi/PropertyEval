import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_ip_address(draw):
    nums = [str(draw(integers(min_value=0, max_value=255))) for _ in range(4)]
    ip = '.'.join(nums)
    return ip

ip = create_ip_address()

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
