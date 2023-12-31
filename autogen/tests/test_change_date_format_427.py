import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import datetime

dt = dates(min_value=datetime.date(1000, 1, 1), max_value=datetime.date(9999, 12, 31)).map(str)
strategy = dt
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, change_date_format, *args)
