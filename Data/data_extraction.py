# MTGJSON Data Extraction Script; Data498-Project 
# Author: Alex Marcek
# Date: 26 October 2026
# Version: 1.0
# Description: Extracts data from the MTGJSON API and saves it to Data/RawDataDumps/JSON/.

# If you dont already have these modules installed, you can install it using pip in the terminal:
# pip install requests

# Import dependencies
import requests
import json
from pathlib import Path

# Function definitions
def save_to_json(data, file_path):
    try:
        if not (file_path.exists() and file_path.is_file()):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
                return f"Data saved to {file_path}"
    
        else:
            return f"File {file_path} already exists."
    
    except Exception as e:
        return f"Error saving data to {file_path}: {e}"

# Clear previous JSON files in the RawDataDumps/JSON directory off of user input
del_files = input("Delete previous session's .json files? (y/n): ").lower()

json_dirpath = Path("Data") / "RawDataDumps" / "JSON"
file_count = 0
if del_files == "y" and (json_dirpath.exists() and json_dirpath.is_dir()):
    for file in json_dirpath.glob("*.json"):
        file.unlink()
        file_count += 1
    print()
    print("Previous session's .json files cleared.")
    print(f"Total .json files cleared: {file_count}")

# Template for extracting data from the MTGJSON API
set_ids = ["SetList"] #--insert set codes of interest here-- "AllPrices"

for id in set_ids:
    url = f"https://mtgjson.com/api/v5/{id}.json"

    response = requests.get(url, timeout=90)
    response.raise_for_status()

    data = response.json()
    print(f"Keys in {id}.json file: {data.keys()}")

    # We want to extract the actual data (data["data"]) from the .json file,
    # METADATA may be important, extract using data["meta"]
    while True:
        desired_data = input("Select top level key: ")
    
        if desired_data.lower() in data.keys():
            data = data[desired_data]
            break
        else:
            print(f"Key '{desired_data}' not found in {id}.json file.")
    

    file_destination = Path("Data") / "RawDataDumps" / "JSON" / f"{id}.json"

    # Save extracted data to file_path
    save_to_json(data, file_destination)
    
