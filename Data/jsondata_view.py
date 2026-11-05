# MTGJSON Extracted JSON file structural analysis; Data498-Project 
# Author: Alex Marcek
# Date: 26 October 2026
# Version: 1.0
# Description: This script is used to analyze the structure of extracted JSON files from the MTGJSON HTTP requests.

# Import modules
from pathlib import Path
import ijson

cwd = Path.cwd()
json_dirpath = Path("Data") / "RawDataDumps" / "JSON"

# Display the .json files 
print(" JSON files available to analyze ".center(80, "-"))
for file in json_dirpath.glob("*.json"):
    print(f"📄 JSON file: {file.stem}")

# Entry to input -> analyze loop
while True:
    file_name = input("Enter the name of the JSON file to analyze (without extension): ").strip()
    file_path = json_dirpath / f"{file_name}.json"

    if file_name.lower() == "/exit":
        break

    elif not file_path.exists() or not file_path.is_file():
        print(f"File '{file_name}.json' not found in {json_dirpath}.")
        continue

    else:
        print(f"Analyzing file '{file_name}.json'...")

        # --WIP
        with open(file_path, "rb") as f:
            parser = ijson.kvitems(f, "") # we use ijson here to preserve memory (top-level) keys
            for key, value in parser:
                print(f"Key: {key}")

                if isinstance(value, dict):
                    print(f"  Sub-keys: {list(value.keys())}")
                elif isinstance(value, list) and len(value) > 0:
                    print(f"  List length: {len(value)}")
                break
