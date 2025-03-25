# PropertyEval
A repository of property-based tests for thorough benchmarking of LLM code generation.

## Citation

If you use or modify this dataset or related tools, please cite it as below.

```bibtex
@software{propertyEval,
    author  = {Pawagi, Mrigank},
    doi     = {10.5281/zenodo.15081893},
    title   = {{PropertyEval: Synthesizing Thorough Test Cases for LLM Code Generation Benchmarks using Property-Based Testing}},
    url     = {https://github.com/mrigankpawagi/PropertyEval},
    year    = {2025}
}
```

## Usage
The `/tests` directory contains directories labeled from `0` to `163`, each of which contains a `strategy.py` file. This file contains the [hypothesis strategy](https://hypothesis.readthedocs.io/en/latest/index.html) for the corresponding problem from the [HumanEval](https://github.com/openai/human-eval) dataset. `__init__.py` files have been placed in each directory to allow for importing of the tests as modules. The strategies are available as the `strategy` attribute of these `strategy` modules. Usage of the strategies is as follows.

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

## Contribution

### Thoroughness
We show that it is possible to improve the thoroughness of programming benchmarks using Property-Based Testing (PBT), leveraging the canonical solutions within these benchmarks. For the HumanEval dataset, since adequate property-based tests cannot be automatically generated using rule-based tools, we carefully construct these tests manually. We show that our approach using PBT allows us to synthesize as thorough test cases as those generated using type-aware mutations in Liu et al.'s EvalPlus[^2]. However, our approach can be easily adapted to other contexts.

![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_1.png)
![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_10.png)
![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_100.png)
![](https://github.com/mrigankpawagi/PropertyEval/blob/main/reports/pass_1_greedy.png)

### Dataset
We share our full set of property-based tests as a complementary resource to existing manual and synthesized test suites.

#### Examples

A non-trivial strategy.
```python
# HumanEval 129: minPath
@composite
def create_grid(draw, n_st=integers(min_value=2, max_value=MAX_SEQUENCE_LEN)):
    n = draw(n_st)
    grid = draw(lists(lists(integers(), min_size=n, max_size=n), min_size=n, max_size=n))    
    perm = draw(permutations(range(1, n**2 + 1)))
    # fill grid with perm
    for i in range(n):
        for j in range(n):
            grid[i][j] = perm[i*n + j]    
    return grid

grid = create_grid()
k = integers(min_value=1, max_value=MAX_INT)
strategy = grid, k
```

Examples of additional constraints on the input space. Here, we have restricted the alphabet and introduced bounds on the lengths of strings and lists.
```python
# HumanEval 134: check_if_last_char_is_a_letter
txt = text(alphabet='abcde0123 ')
strategy = txt
```
```python
# HumanEval 143: words_in_sentence
sentence = text(alphabet="a ", min_size=1, max_size=100)
    .map(lambda s: re.sub(r"\s+", " ", s))
    .filter(lambda s: not (s.startswith(" ") or s.endswith(" ")))
strategy = sentence
```
```python
# HumanEval 158: find_max
words = lists(text(alphabet='abc', max_size=MAX_SEQUENCE_LEN), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = words
```

> [!TIP]
> The [ghAIstwriter](https://github.com/mrigankpawagi/ghAIstwriter) project uses these strategies to create a dataset for finetuning LLMs to generate such strategies automatically.

### Automation
For the [MBPP](https://github.com/google-research/google-research/tree/master/mbpp) dataset, we demonstrate that these tests can be generated largely automatically using GPT-3.5 by providing few-shot prompts based on some of our manually constructed tests. This demonstrates that our approach can be easily scaled to other datasets.

> [!WARNING]  
> This is a work in progress, but some preliminary results are available [here](https://github.com/mrigankpawagi/PropertyEval/tree/main/autogen).

![image](https://github.com/mrigankpawagi/PropertyEval/assets/25179158/f10b9adf-36a9-45e0-a00b-1e89aa0aa077)

### Contributing back to EvalPlus
Work on PropertyEval has led to several contributions to EvalPlus as suggestions for improving contracts in many problems. These have been acknowledged by the authors of EvalPlus and incorporated in their subsequent releases.

- [Incomplete contracts in problems involving balanced parantheses (1, 6)](https://github.com/evalplus/evalplus/issues/27)
- [Contract misses infinities and nan (2, 99)](https://github.com/evalplus/evalplus/issues/28)
- [Contract misses empty list in problem 35](https://github.com/evalplus/evalplus/issues/29)
- [Incomplete contract in HumanEval #32 (`find_zero`)](https://github.com/evalplus/evalplus/issues/34)
- [Incomplete contract in HumanEval #160 (`do_algebra`)](https://github.com/evalplus/evalplus/issues/35)

## Evaluation
The `/humaneval_groundtruth` directory contains canonical solutions to HumanEval problems, adapted from the ground truth solutions provided with [EvalPlus v0.1.0](https://github.com/evalplus/evalplus/releases/tag/v0.1.0). The results from the equivalence tests on code samples for 84 _(model, size, temperature)_ combinations provided with EvalPlus v0.1.0 are available in `evaldata.csv`. The script for executing this benchmark is a modified fork[^1] of the EvalPlus script. 

The `limits/limits.py` file contains several standardized limits for the strategies. The `limits/fuzzer.py` script is for running fuzz-tests on all HumanEval ground truth with the strategies in order to validate these limits.

[^1]: We forked [EvalPlus](https://github.com/evalplus/evalplus) and modified the evaluation script to evaluate code samples with PropertyEval's property-based tests as well, in addition to the `Base` and `Base + Extra` test cases. We further modified the existing pipeline for estimating _pass@k_ for PropertyEval's property-based tests also. The fork is available as [EvalPlusPro](https://github.com/mrigankpawagi/evalpluspro). Some points to note are as follows.

    1. The property-based tests are executed with 1000 examples, with `@settings(max_examples=1000)`.
    2. Instead of the time limits enforced by EvalPlus, we use the default deadline of 200ms that comes with Hypothesis.

[^2]: Jiawei Liu et al. “Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation”. In: _arXiv preprint arXiv:2305.01210 (2023)_
