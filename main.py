import os
import json
from drill_utils import process_machine

raw_dir = "data/raw"
processed_dir = "data/processed"
os.makedirs(processed_dir, exist_ok=True)

files = [f for f in os.listdir(raw_dir) if f.endswith(".json")]

for filename in files:
    in_path = os.path.join(raw_dir, filename)
    with open(in_path, "r") as f:
        data = json.load(f)
    processed = process_machine(data)
