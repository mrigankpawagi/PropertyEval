import importlib
import json
from hypothesis import strategies, given

HUMANEVAL_DATA = "../problems.json" # Path to the problems.json file

with open(HUMANEVAL_DATA) as f:
    problems_data = json.load(f)

for i in range(164):
    task_id = str(i)
    entry_point = problems_data[f"HumanEval/{task_id}"]["entry_point"]
    pre = task_id.zfill(3)

    # Get the strategy
    st_module = importlib.import_module(f"tests.{task_id}.strategy")
    st = st_module.strategy
    if not isinstance(st, tuple):
        st = (st,)

    # Get the groundtruth
    gt_module = importlib.import_module(f"humaneval_groundtruth.{pre}_{entry_point}")
    gt_func = getattr(gt_module, entry_point)

    # fuzz
    faulty_args = None
    
    @given(strategies.tuples(*st))
    def test_fuzz(args):
        global faulty_args
        faulty_args = args
        gt_func(*args)

    try:
        test_fuzz()
    except Exception as e:
        print(f"{e} for {task_id}: {entry_point} with {faulty_args}")
