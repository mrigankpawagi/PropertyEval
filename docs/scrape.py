import csv

with open('../evaldata.csv') as f:
    data = list(csv.reader(f))
    
temp0_pass1_list_base = []
temp0_pass1_list_prop = []
    
for item in data:
    model = item[0]

    metric = item[1]
    pass1 = item[2]
    
    # Get Temperature 0, Pass@1 for Base and PropertyEval
    if model.endswith('0_0') and metric in ('Base', 'PropertyEval'):
        if metric == 'Base':
            temp0_pass1_list_base.append([model, metric, pass1])
        elif metric == 'PropertyEval':
            temp0_pass1_list_prop.append([model, metric, pass1])

# # #

temp0_pass1_list_base.sort(key=lambda x: x[2], reverse=True)
temp0_pass1_list_prop.sort(key=lambda x: x[2], reverse=True)

for item in temp0_pass1_list_base:
    print(item)
print("---")
for item in temp0_pass1_list_prop:
    print(item)
