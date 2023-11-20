import json
from main import generate

with open("../problems.json") as f:
    problems = json.load(f)
    
k = 0

for key in problems:
    if k in {0, 6, 11, 26, 115}: # problems included for few-shot learning
        k += 1
        continue
    
    prompt = problems[key]["prompt"]
    
    # remove everything before the first "def"
    prompt = prompt[prompt.find("def"):]
    
    print(generate(prompt)[0])
    print("-"*80)
    
    k += 1
    if k > 10:
        break
