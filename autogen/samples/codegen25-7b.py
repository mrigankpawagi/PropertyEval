from transformers import pipeline, AutoTokenizer
import json
import os
from util import tasks_list, dataset

pipe = pipeline(
    "text-generation", 
    model="Salesforce/codegen25-7b-mono", 
    tokenizer="Salesforce/codegen25-7b-mono", 
    trust_remote_code=True
)

if not os.path.exists("models/codegen25_7b_temp_0_0"):
    os.mkdir("models/codegen25_7b_temp_0_0")

for problem in dataset:
    task_id = problem["task_id"]
    if task_id not in tasks_list:
        continue
    
    description = problem["prompt"]
    test_list = problem["test_list"]
    code: str = problem["code"]

    entry_point = code[code.rfind("def "):].split("def ")[1].split("(")[0].strip()
    signature = code[:code.find("\n", code.rfind("def "))]

    
    # Incoder style prompt inspired from https://github.com/bigcode-project/bigcode-evaluation-harness/blob/main/docs/README.md#mbpp
    # code1 = "def find_Min_Sum(num): \n    sum = 0\n    i = 2\n    while(i * i <= num): \n        while(num % i == 0): \n            sum += i \n            num /= i \n        i += 1\n    sum += num \n    return sum"
    # shot1 = '"""\nWrite a python function to find minimum sum of factors of a given number.\nassert find_Min_Sum(12) == 7\n"""\n' + code1 + '\n[\END\]\n\n'
    
    # code2 = "def flatten(test_tuple): \n\tfor tup in test_tuple: \n\t\tif isinstance(tup, tuple): \n\t\t\tyield from flatten(tup) \n\t\telse: \n\t\t\tyield tup \ndef count_element_freq(test_tuple):\n  res = {}\n  for ele in flatten(test_tuple):\n    if ele not in res:\n      res[ele] = 0\n    res[ele] += 1\n  return (res)"
    # shot2 = '"""\nWrite a function to count the element frequency in the mixed nested tuple.\nassert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9) ) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}\n"""\n' + code2 + '\n[\END\]\n\n'
    
    # Completion-style prompt
    prompt = f'{signature}\n  """\n  {description}\n  {test_list[0].replace("assert", ">>>")}\n  """\n'

    if not os.path.exists(f"models/codegen25_7b_temp_0_0/{task_id}"):
        os.mkdir(f"models/codegen25_7b_temp_0_0/{task_id}")
    
    for i in range(1):
        response = pipe(
            prompt,
            max_new_tokens=75,
            temperature=0.0
        )
        
        program = response[0]["generated_text"]
        print(f"---------\n{task_id}.{i}---------\n", program)
        with open(f"models/codegen25_7b_temp_0_0/{task_id}/{i}.py", "w") as f:
            f.write(program)
