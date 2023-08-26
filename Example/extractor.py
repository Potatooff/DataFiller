import os
from json import load, dump
from string import punctuation
from aa import get_response
from aa import similarity
from cachetools import cached, TTLCache


current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.join(current_dir, "..")
current_dir = os.path.join(current_dir, "..")
data_dir = os.path.join(current_dir, "data")
raw_dir = os.path.join(data_dir, "raw")
intentsjson_dir = os.path.join(raw_dir, "school.json")
CACHE_SIZE = 99999999999999999999999  
CACHE_TIMEOUT = 7000000000000000000000000000
cache = TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TIMEOUT)


# Read data from the JSON file
with open(intentsjson_dir, 'r') as file:
    data = load(file)


"""Remove punctuation, Lower string"""
@cached(cache)
def clean_text(text):
    text = f"{text}"
    corrected = text.lower()
    cleaned_text = corrected.translate(str.maketrans("", "", punctuation))
    return cleaned_text

# Change "responses" or "patterns" with the tag you want to be extract + buffed
# produce multi sentence with the same meaning
@cached(cache)
def bigger_data():  
    for intent in data["intents"]:  # each tag intents
        upgraded = []
        extracted = []
        extracted = intent["responses"] 
        print(extracted)    # Extracted Data
        for j in extracted:  # for each string in responses
            j = clean_text(j)      
            upgraded.append(j)
            results = []
            try:
                result = get_response(j, 20, 30)    # Result is a list of string of datafiller result
            except IndexError:
                print("NO") # Error handler
                continue
            for o in result:    # for each string in result list
                o = clean_text(o)
                score = similarity(j, o)    # get a similitray between the two sentence
                if score > 72:  # if score = 70 its doesnt show up in the final data
                    results.append(o)
            for k in results:
                upgraded.append(k)
        upgraded_set = set(upgraded)
        intent["responses"] = list(upgraded_set)
        with open(intentsjson_dir, 'w') as file:
            dump(data, file, indent=4) 
        print(f"{upgraded_set}\n")  # Filled Data
        
