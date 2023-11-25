## Generating strategies automatically using few-shot prompting on GPT-3.5 Turbo
We use some of the hand-crafted strategies created for HumanEval to provide a few-shot prompt to GPT-3.5 Turbo for generating strategies for the Sanitized MBPP dataset. We then fuzz the ground truths available in MBPP using these strategies, and out of 427 strategies (for the 427 problems in sanitized MBPP), 364 (over 85%) strategies were valid. We then manually fixed the remaining strategies.

We then utilize the code samples for 22 (model, size, temperature) combinations provided with [EvalPlus v0.2.0](https://github.com/evalplus/evalplus/releases/tag/v0.2.0) to evaluate the samples using these strategies. There are 338 problems in the intersection of our strategies and the code samples provided by EvalPlus. This is the set of problems we use for our evaluation.


<!-- | Model | Base | PropertEval | Base + PropertyEval |
| --- | --- | --- | --- |
| starcoder_temp_0_0 | 100.00 | 84.62 | 84.62 |
| codet5p-2b_temp_0_0 | 99.41 | 84.02 | 84.02 |
| codet5p-6b_temp_0_0 | 99.41 | 84.02 | 84.02 |
| codet5p-16b_temp_0_0 | 99.11 | 84.02 | 84.02 |
| deepseek-coder-6_7b-base_temp_0 | 98.52 | 83.14 | 83.14 |
| wizardcoder-15b_temp_0_0 | 97.93 | 83.14 | 83.14 |
| gpt-3 | 97.93 | 83.14 | 83.14 |
| deepseek-coder-1_3b-base_temp_0_0 | 97.93 | 82.84 | 82.84 |
| wizardcoder-34b_temp_0 | 97.04 | 82.25 | 82.25 |
| deepseek-coder-33b-instruct_temp_0 | 97.04 | 82.25 | 82.25 |
| code-llama-34b_temp_0 | 96.75 | 81.66 | 81.66 |
| deepseek-coder-1_3b-instruct_temp_0_0 | 96.15 | 81.36 | 81.36 |
| code-llama-13b_temp_0 | 96.15 | 81.36 | 81.36 |
| zephyr-7b_temp_0 | 94.97 | 81.36 | 81.36 |
| mistral-7b_temp_0_0 | 95.56 | 80.77 | 80.77 |
| codegen-16b_temp_0_0 | 94.97 | 80.77 | 80.77 |
| gpt-4-1106-preview_temp_0_0 | 95.56 | 80.18 | 80.18 |
| codegen-6b_temp_0_0 | 94.67 | 80.18 | 80.18 |
| codegen-2b_temp_0 | 93.20 | 78.40 | 78.40 |
| wizardcoder-7b_temp_0_0 | 92.01 | 77.81 | 77.81 |
| code-llama-7b_temp_0_0 | 91.72 | 76.92 | 76.92 |
| deepseek-coder-6_7b-instruct_temp_0_0 | 90.83 | 76.63 | 76.63 | -->
