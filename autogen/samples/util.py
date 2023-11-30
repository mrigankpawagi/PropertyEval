import sys
sys.path.extend(["../../..", "../..", ".."])

import json
from timeout import timeout, run_with_timeout
from typing import *
from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
import importlib
import string
import math
import pickle

tasks_list = set()

with open("../pytest.log") as f:
    for line in f.readlines():
        if line.startswith("tests/"):
            l = line.strip()
            file, status = l.split()[:2]
            if status.strip() == ".":
                n = int(file.strip().split(".py")[0].split("_")[-1])
                tasks_list.add(n)

with open ("../../sanitized-mbpp.json") as f:
    dataset = json.load(f)

with open ("../gen.json") as f:
    properteval_dataset_list = json.load(f)
    # convert to a dict with keys as task_id
    properteval_dataset = {}
    for problem in properteval_dataset_list:
        properteval_dataset[problem["task_id"]] = problem
        del problem["task_id"]

mbppplus_tests = {}        
with open("mbppplus.json") as f:
    mbppplus_dataset = json.load(f)
    for problem in mbppplus_dataset:
        task_id = int(problem["task_id"].split("/")[-1])
        mbppplus_tests[task_id] = problem["plus_input"]

def base_test(completion: str, test_list: list[str], entry_point: str) -> bool:
    completion_with_timeout = completion.replace(f"def {entry_point}", f"@timeout()\ndef {entry_point}", 1)
    tests = "\n".join([f"  {test}" for test in test_list])

    try:
        exec(f"""{completion_with_timeout}

def test_base():
  global {entry_point}
{tests}

run_with_timeout(10, test_base)""", globals()) # Very high timeout to ensure that all tests are run
        return True
    except Exception as e:
        # print(f"BASE ERR {entry_point}:", e)
        return False    

def properteval_test(completion: str, strategy: str, entry_point: str, task_id: int) -> bool:
    try:
        exec(f"""gt_module = importlib.import_module("groundtruth.{task_id}")
gt_func = getattr(gt_module, entry_point)

{completion}

{strategy}
if not isinstance(strategy, tuple):
    strategy = (strategy,)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_properteval(args):
    global {entry_point}, gt_func
    assert {entry_point}(*args) == gt_func(*args)
    
run_with_timeout(600, test_properteval)""", globals(), locals()) # 1000 * 0.3 * 2 = 600

        return True
    except Exception as e:
        # print(f"PROP ERR {entry_point}:", e)
        return False    

def mbppplus_test(completion: str, entry_point: str, task_id: int) -> bool:    
    with open("/home/mrigankp/.cache/evalplus/ebe95df0d5220f00cedd6f4bddea35e4.pkl", "rb") as f:
        expected = pickle.load(f)

    try:
        exec(f"""{completion}

def test_mbppplus(args, expected_answer):
    global {entry_point}
    assert {entry_point}(*args) == expected_answer

for inp, time_limit, expected_answer in zip(mbppplus_tests[task_id], expected[f"Mbpp/{task_id}"]["plus_time"], expected[f"Mbpp/{task_id}"]["plus"]):
    run_with_timeout(max(0.3, time_limit), test_mbppplus, inp, expected_answer)""", globals(), locals())

        return True
    except Exception as e:
        # print("MBBP ERR:", e)
        return False    
