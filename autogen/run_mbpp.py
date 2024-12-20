import json
from main import generate_strategy

def generate_input(prompt, code, tests, entry_point):
    # if there is no def in the code, throw an error
    if code.find("def") == -1:
        raise Exception("No function definition found in code.")
    
    # Synthesise docstring
    doctests = [test.split("assert ")[1] for test in tests]
    doctests_string = "".join([f"  >>> {doctest}\n  True\n" for doctest in doctests])
    docstring = f'''  """{prompt}\n{doctests_string}  """\n'''
    
    # extract function signature
    def_position = code.find(f"def {entry_point}")
    synthesised_prompt = code[:1 + code.find("\n", def_position)] + docstring + code[code.find("\n", def_position)+1:]
    
    return synthesised_prompt
    

with open("../sanitized-mbpp.json") as f:
    problems = json.load(f)
   
with open("samples/mbppplus.json") as f:
    mbppplus_dataset_array = json.load(f)
    mbppplus_dataset = {}
    for entry in mbppplus_dataset_array:
        mbppplus_dataset[entry["task_id"]] = entry 

k = 0

dataset = []

for problem in problems:
    task_id = problem["task_id"]
    prompt = problem["prompt"]
    code = problem["code"]
    tests = problem["test_list"]
    
    try:
        entry_point = mbppplus_dataset[f"Mbpp/{task_id}"]["entry_point"]
        synthesised_prompt = generate_input(prompt, code, tests, entry_point)
    except:
        continue

    try:
        strategy = generate_strategy(synthesised_prompt)[0]
        dataset.append({
            "task_id": task_id,
            "prompt": synthesised_prompt,
            "strategy": strategy,
            "code": code
        })
        print(f"Generated strategy for task {task_id}")
    except:
        continue
    
    k += 1
    print(f"Completed {k} tasks.")

with open("gen.json", "w") as f:
    json.dump(dataset, f, indent=4)
