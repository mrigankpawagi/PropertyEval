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
                raw_completion = f.read() + "\n"

        except Exception as e:
            continue # skip if this task is not in the model
        
        entry_point_index = raw_completion.find(f"def {entry_point}")
        
        # remove any statements after the entry point definition
        new_line_positions = [i for i, c in enumerate(raw_completion) if c == "\n" and i > entry_point_index]
        if len(new_line_positions) > 0:
            function_end_index = new_line_positions[-1]
            for i in new_line_positions:
                # check if this line starts with indentation
                if i + 1 < len(raw_completion) and raw_completion[i + 1] != " ":
                    function_end_index = i
                    break
            completion = raw_completion[:function_end_index]

        # remove anything before the entry point definition that is not an import or another function definition
        # this is to remove stray text or comments
        new_line_positions = [i for i, c in enumerate(completion) if c == "\n" and i < entry_point_index]
        if len(new_line_positions) > 0:
            code_start_index = new_line_positions[-1]
            for i in new_line_positions:
                if completion[i: i + 4] == "def " or completion[i: i + 7] == "import " or completion[i: i + 5] == "from ":
                    code_start_index = i
                    break
            completion = completion[code_start_index:]               
            
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
