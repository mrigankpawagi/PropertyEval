import json

with open("gen.json") as f:
    problems = json.load(f)
    
print(f"Total problems: {len(problems)}")

for problem in problems:
    task_id = problem["task_id"]
    prompt = problem["prompt"]
    strategy_completion = problem["strategy"]
    code = problem["code"]
    
    entry_point = code.split("def ")[1].split("(")[0].strip()
    test_fuzz = None
    
    code_with_timeout = code.replace("def ", "@timeout()\ndef ", 1)

    with open(f"tests/test_{entry_point}_{task_id}.py", "w") as f:
        f.write(f"""import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import timeout
from typing import *
                
{strategy_completion}
if not isinstance(strategy, tuple):
    strategy = (strategy,)

{code_with_timeout}

@given(tuples(*strategy))
def test_fuzz(args):
    {entry_point}(*args)\n""")
