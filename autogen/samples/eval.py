import json
import os
from util import tasks_list, dataset, properteval_dataset, base_test, properteval_test

def evaluate(model):
    results = {}

    for problem in dataset:
        task_id = problem["task_id"]
        if task_id not in tasks_list:
            continue

        test_list = problem["test_list"]
        code: str = problem["code"]
        strategy = properteval_dataset[task_id]["strategy"]
        
        entry_point = code[code.rfind("def "):].split("def ")[1].split("(")[0].strip()
        
        try:
            with open(f"models/{model}/Mbpp_{task_id}/0.py", "r") as f:
                raw_completion = f.read()
            print(f"Testing {model} on {task_id} ({entry_point})...")
        except Exception as e:
            continue # skip if this task is not in the model
        
        entry_point_index = raw_completion.find(f"def {entry_point}")
        
        # remove any def statements after the entry point definition
        if raw_completion.find("def ", entry_point_index + 1) != -1:
            completion = raw_completion[:raw_completion.find("def ", entry_point_index + 1)]
        else:
            completion = raw_completion
            
        base = base_test(completion, test_list, entry_point)
        properteval = properteval_test(completion, strategy, code, entry_point, task_id)
        
        results[task_id] = {
            "base": base,
            "properteval": properteval
        }

    statistics = {
        "total": len(results),
        "base": len([1 for task_id in results if results[task_id]["base"]]),
        "properteval": len([1 for task_id in results if results[task_id]["properteval"]]),
        "both": len([1 for task_id in results if results[task_id]["base"] and results[task_id]["properteval"]])
    }

    with open(f"results/{model}.json", "w") as f:
        json.dump({
            "statistics": statistics,
            "results": results
        }, f, indent=4)

if __name__ == "__main__":
    for model in os.listdir("models"):
        print(f"Evaluating {model}...")
        evaluate(model)
