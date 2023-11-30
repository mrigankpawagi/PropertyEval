import json
import os

print("| Model | Base | PropertEval | MBPP+ | Base + PropertyEval | Base + MBPP+ |")
print("| --- | --- | --- | --- | --- | --- |")

resultsdata = []

with open("models/list.txt") as f:
    models = f.read().splitlines()

for model in models:
    name = model.split(".")[0]
    with open(f"results/{model}.json") as f:
        data = json.load(f)
        statistics = data["statistics"]
        
        base = 100 * statistics["Base"] / statistics["Total"]
        properteval = 100 * statistics["PropertyEval"] / statistics["Total"]
        base_propertyeval = 100 * statistics["Base + PropertyEval"] / statistics["Total"]
        mbpp_plus = 100 * statistics["MBPP+"] / statistics["Total"]
        base_mbpp_plus = 100 * statistics["Base + MBPP+"] / statistics["Total"]
        
        resultsdata.append({
            "name": name,
            "base": base,
            "properteval": properteval,
            "base+properteval": base_propertyeval,
            "mbpp+": mbpp_plus,
            "base+mbpp+": base_mbpp_plus,
        })

# Print in descending order of base + properteval
resultsdata.sort(key=lambda x: x["base+properteval"], reverse=True)
for model in resultsdata:
    print(f"| {model['name']} | {model['base']:.2f} | {model['properteval']:.2f} | {model['mbpp+']:.2f} | {model['base+properteval']:.2f} | {model['base+mbpp+']:.2f} |")
