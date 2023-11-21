import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
string = text(alphabet=string.ascii_letters + string.digits, min_size=1)
strategy = string,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def string_to_list(string): 
    lst = list(string.split(" ")) 
    return lst

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, string_to_list, *args)
