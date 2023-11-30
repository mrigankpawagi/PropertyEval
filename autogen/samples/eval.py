import json
import os
from util import tasks_list, dataset, properteval_dataset, base_test, properteval_test, mbppplus_test

def evaluate(model):
    results = {}

    k = 0
    for problem in dataset:
        task_id = problem["task_id"]
        if task_id not in tasks_list:
            continue

        test_list = problem["test_list"]
        code: str = problem["code"]
        strategy = properteval_dataset[task_id]["strategy"]
        
        entry_point = code[code.rfind("def "):].split("def ")[1].split("(")[0].strip()
        
        # Noted exceptions
        exceptions = {
            6: "differ_At_One_Bit_Pos",
            70: "find_equal_tuple",
            580: "even_ele",
            592: "binomial_Coeff",
            630: "adjac",
            797: "sum_odd",
        }
        if task_id in exceptions:
            entry_point = exceptions[task_id]
        
        try:
            with open(f"models/{model}/Mbpp_{task_id}/0.py", "r") as f:
                raw_completion = f.read() + "\n"

        except Exception as e:
            continue # skip if this task is not in the model
        
        k += 1
        print(f"Doing {k}/399: {entry_point}/{task_id}")
        
        # Completions were sanitized using evalplus/tools/sanitize.py
        completion = raw_completion
            
        # save groundtruth if not exists
        if not os.path.exists(f"groundtruth/{task_id}.py"):
            with open(f"groundtruth/{task_id}.py", "w") as f:
                f.write(code)         
            
        base = base_test(completion, test_list, entry_point)
        properteval = properteval_test(completion, strategy, entry_point, task_id)
        mbppplus = mbppplus_test(completion, entry_point, task_id)
        
        results[task_id] = {
            "base": base,
            "properteval": properteval,
            "mbppplus": mbppplus
        }

    statistics = {
        "Total": len(results),
        "Base": len([1 for task_id in results if results[task_id]["base"]]),
        "PropertyEval": len([1 for task_id in results if results[task_id]["properteval"]]),
        "MBPP+": len([1 for task_id in results if results[task_id]["mbppplus"]]),
        "Base + PropertyEval": len([1 for task_id in results if results[task_id]["base"] and results[task_id]["properteval"]]),
        "Base + MBPP+": len([1 for task_id in results if results[task_id]["base"] and results[task_id]["mbppplus"]])
    }

    with open(f"results/{model}.json", "w") as f:
        json.dump({
            "statistics": statistics,
            "results": results
        }, f, indent=4)

if __name__ == "__main__":
    with open ("models/list.txt") as f:
        models = f.read().splitlines()    
    for model in models:
        print(f"Evaluating {model}...")
        evaluate(model)
