import json

file_path = "Data/RawDataDumps/JSON/SetList.json"

def extract_keys(data, keys_set=None):
    if keys_set is None:
        keys_set = set()

    if isinstance(data, dict):
        for key, value in data.items():
            keys_set.add(key)
            extract_keys(value, keys_set) # recursive descent into nested dictionaries

    elif isinstance(data, list):
        for item in data:
            extract_keys(item, keys_set)

    return keys_set

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data[0]["decks"][0]["mainBoard"][0]["count"])

# Basic structure of SetList.json
print(len(data)) # there are 879 sets
print(data[0].keys()) # keys in the first set

#all_keys = list(extract_keys(data))
#print(all_keys)