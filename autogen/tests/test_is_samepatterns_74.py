import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_colors_and_patterns(draw):
    n = draw(integers(min_value=1, max_value=100))
    colors = draw(lists(text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=n, max_size=n), min_size=n, max_size=n))
    patterns = draw(lists(text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=n, max_size=n), min_size=n, max_size=n))
    return colors, patterns

colors, patterns = create_colors_and_patterns()

strategy = colors, patterns
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_samepatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False    
    sdict = {}
    pset = set()
    sset = set()    
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []

        keys = sdict[patterns[i]]
        keys.append(colors[i])
        sdict[patterns[i]] = keys

    if len(pset) != len(sset):
        return False   

    for values in sdict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_samepatterns, *args)
