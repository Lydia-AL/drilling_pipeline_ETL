import os
import json
from drill_utils import process_machine, remove_useless_data, convert_dates, convert_miles_to_meters, add_contact_info, format_machine_id

raw_dir = "data/raw"
processed_dir = "data/processed"
os.makedirs(processed_dir, exist_ok=True)

files = sorted([f for f in os.listdir(raw_dir) if f.endswith(".json")])

for filename in files:
    in_path = os.path.join(raw_dir, filename)
    out_path = os.path.join(processed_dir, filename)

    with open(in_path, "r") as f:
        data = json.load(f)

    #ETL pipeline
    processed = process_machine(data)

    with open(out_path, "w") as f:
        json.dump(processed, f, indent=2)

    print(f"Processed {in_path} -> {out_path}")

