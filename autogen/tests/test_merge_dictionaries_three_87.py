import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
dict1 = dictionaries(keys=text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower()), values=integers())
dict2 = dictionaries(keys=text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower()), values=integers())
dict3 = dictionaries(keys=text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower()), values=integers())

strategy = dict1, dict2, dict3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import collections as ct
def merge_dictionaries_three(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))
    return merged_dict

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, merge_dictionaries_three, *args)
