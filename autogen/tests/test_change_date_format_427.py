import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import datetime

def get_date():
    year = integers(min_value=1000, max_value=9999)
    month = integers(min_value=1, max_value=12)
    day = integers(min_value=1, max_value=31)
    date = year.flatmap(lambda y: month.flatmap(lambda m: day.map(lambda d: (y, m, d))))
    return date.map(lambda x: datetime.date(*x))

dt = get_date()

strategy = dt
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, change_date_format, *args)
