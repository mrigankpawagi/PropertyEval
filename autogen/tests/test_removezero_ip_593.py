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
                
ip = from_regex(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

strategy = ip,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def removezero_ip(ip):
 string = re.sub('\.[0]*', '.', ip)
 return string


@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, removezero_ip, *args)
