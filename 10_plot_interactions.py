# --- Day2 Step4: Visualization ---
import csv, collections, matplotlib.pyplot as plt

path = "data/drug_interactions.csv"
counts = collections.Counter()

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        lvl = row['interaction_level'].strip().capitalize() or "Unknown"
        counts[lvl] += 1

levels = list(counts.keys())
values = list(counts.values())

plt.bar(levels, values)
plt.title("Drug Interaction Levels (AtlasAgent Data)")
plt.xlabel("Interaction Level")
plt.ylabel("Count")
plt.savefig("interaction_counts.png")
plt.close()

print("Chart saved as interaction_counts.png")
