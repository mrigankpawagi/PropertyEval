# PropertyEval
A repository of property-based tests for thorough benchmarking of LLM code generation.

## Property-based tests
The `/tests` directory contains directories labelled from `0` to `163`, each of which contains a `strategy.py` file. This file contains the hypothesis strategy for the corresponding problem from the HumanEval dataset. `__init__.py` files have been placed in each directory to allow for importing of the tests as modules. The strategies are available as the `strategy` attribute of these `strategy` modules. Usage of the strategies is as follows.

```python
from hypothesis import given, strategies

@given(strategies.tuples(*st))
def test_property(args):
    # call functions as f(*args)
    # for example, assert f(*args) == ground_truth(*args)
    # ...
```

Here, `st` is the imported strategy. One way to do this is using the `importlib` module.

```python
import importlib

st_module = importlib.import_module(f"test.{humaneval_id}.strategy")
st = st_module.strategy
```

## Evaluation
The `/humaneval_groundtruth` directory contains canonical solutions to HumanEval problems, adapted from the groundtruths provided with [EvalPlus v0.1.0](https://github.com/evalplus/evalplus/releases/tag/v0.1.0). The results from the equivalence tests on code samples for 84 _(model, size, temperature)_ combinations provided with EvalPlus v0.1.0 are available in `evaldata.csv`. The script for executing this benchmark is a modified fork of the EvalPlus* script. 

1. _pass@k_ for `Base`
2. _pass@k_ for `Base + Extra`
3. _pass@k_ for PropertyEval

The `limits/limits.py` file contains several standardized limits for the strategies. The `limits/fuzzer.py` script is for running fuzz-testing on all HumanEval groundtruths with the strategies.

## Comparison with EvalPlus

![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_1.png)
![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_10.png)
![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_100.png)
![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_1_greedy.png)

### *Fork of EvalPlus

We forked [EvalPlus](https://github.com/evalplus/evalplus) and modified the evaluation script to evaluate code samples with PropertyEval's property-based tests as well, in addition to the `Base` and `Base + Extra` test cases. We further used the same functions for estimating _pass@k_ for PropertyEval's property-based tests. The fork is available as [EvalPlusPro](https://github.com/mrigankpawagi/evalpluspro). Some points to note are as follows.

1. The property-based tests are executed with 1000 examples, with `@settings(max_examples=1000)`.
2. Instead of the time limits enforced by EvalPlus, we use the default deadline of 200ms that comes with Hypothesis.
