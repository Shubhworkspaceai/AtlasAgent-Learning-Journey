# --- Day2 Step3: CSV Analysis ---
import csv, collections

path = "data/drug_interactions.csv"

counts = collections.Counter()

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        lvl = row['interaction_level'].strip().lower() or "unknown"
        counts[lvl] += 1

print("Interaction level counts:")
for level, n in counts.items():
    print(f"{level}: {n}")
