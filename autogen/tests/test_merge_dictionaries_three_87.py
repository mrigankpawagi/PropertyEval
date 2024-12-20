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
                
dict1 = dictionaries(text(), text())
dict2 = dictionaries(text(), text())
dict3 = dictionaries(text(), text())

strategy = dict1, dict2, dict3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import collections as ct
def merge_dictionaries_three(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))
    return merged_dict

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, merge_dictionaries_three, *args)
