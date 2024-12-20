import json

with open("gen.json") as f:
    problems = json.load(f)
   
with open("samples/mbppplus.json") as f:
    mbppplus_dataset_array = json.load(f)
    mbppplus_dataset = {}
    for entry in mbppplus_dataset_array:
        mbppplus_dataset[entry["task_id"]] = entry
    
print(f"Total problems: {len(problems)}")

for problem in problems:
    task_id = problem["task_id"]
    prompt = problem["prompt"]
    strategy_completion = problem["strategy"]
    code = problem["code"]
    
    entry_point = mbppplus_dataset[f"Mbpp/{task_id}"]["entry_point"]
    test_fuzz = None

    with open(f"tests/test_{entry_point}_{task_id}.py", "w") as f:
        f.write(f"""import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
{strategy_completion}
if not isinstance(strategy, tuple):
    strategy = (strategy,)

{code}

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, {entry_point}, *args)\n""")

import os
os.system("pytest tests/ --tb=no --continue-on-collection-errors -k 'not test_test_duplicate and not test_test_three_equal' > pytest.log 2>&1")
