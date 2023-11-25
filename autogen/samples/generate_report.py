import json
import os

print("| Model | Base | PropertEval | Base + PropertyEval |")
print("| --- | --- | --- | --- |")

resultsdata = []

for model in os.listdir("results"):
    name = model.split(".")[0]
    with open(f"results/{model}") as f:
        data = json.load(f)
        statistics = data["statistics"]
        
        base = 100 * statistics["base"] / statistics["total"]
        properteval = 100 * statistics["properteval"] / statistics["total"]
        both = 100 * statistics["both"] / statistics["total"]
        
        resultsdata.append({
            "name": name,
            "base": base,
            "properteval": properteval,
            "both": both
        })

# Print in descending order of base + properteval
resultsdata.sort(key=lambda x: x["both"], reverse=True)
for model in resultsdata:
    print(f"| {model['name']} | {model['base']:.2f} | {model['properteval']:.2f} | {model['both']:.2f} |")
