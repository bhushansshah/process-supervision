import os
import random
from datasets import load_dataset, load_from_disk

DATA_PATH = "./data/omni_math"

# Check if the dataset is already saved to disk
if os.path.exists(DATA_PATH):
    print("Dataset found on disk. Loading from local storage...")
    ds = load_from_disk(DATA_PATH)
else:
    print("Dataset not found locally. Downloading from Hugging Face...")
    ds = load_dataset("KbsdJames/Omni-MATH")
    ds.save_to_disk(DATA_PATH)
    print(f"Dataset saved to {DATA_PATH}")

# Print dataset overview
print(f"\nDataset: {ds}")
print(f"Number of examples: {len(ds['test'])}")
print(f"Fields: {ds['test'].column_names}")

# Print a random row with all fields
idx = random.randint(0, len(ds['test']) - 1)
row = ds['test'][idx]
print(f"\n--- Random Example (index {idx}) ---")
for field, value in row.items():
    print(f"\n[{field}]")
    print(value)
