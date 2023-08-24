import json
from aa import get_response

# Read data from the JSON file
with open('data1.json', 'r') as file:
    data = json.load(file)

def lowering(asd):
    asd = f"{asd}"
    return asd.lower()

def new_values(new_vales):
    for intent in data["intents"]:
        new_patterns = new_vales
        intent["patterns"] = new_patterns
    with open('data1.json', 'w') as file:
        json.dump(data, file, indent=4)

def bigger_data():  
    for intent in data["intents"]:
        upgraded = []
        extracted = []
        extracted = intent["patterns"]
        print(extracted)
        for j in extracted:        
            upgraded.append(j)
            results = []
            result = get_response(j, 2, 3)
            for o in result:
                o = lowering(o)
                results.append(o)
            for k in results:
                upgraded.append(k)
        upgraded_set = set(upgraded)
        intent["patterns"] = list(upgraded_set)
        with open('data1.json', 'w') as file:
            json.dump(data, file, indent=4)
    
        print(upgraded_set)
        #new_values(list(upgraded_set))
        
        
bigger_data()
