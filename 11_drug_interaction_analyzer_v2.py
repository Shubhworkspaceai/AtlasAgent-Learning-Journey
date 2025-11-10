# --- Analyzer v2 (Weighted Scores) ---
import csv, collections, matplotlib.pyplot as plt, json, os

CSV_PATH = "data/drug_interactions.csv"

# weight mapping requested by you
WEIGHTS = {
    "None": 0.0,
    "Moderate": 1.5,
    "High": 3.0,
    "Unknown": 0.0
}

def load_data(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def normalize_level(value):
    if not value:
        return "Unknown"
    return value.strip().lower().capitalize()

def summarize_counts(data):
    counts = collections.Counter()
    for row in data:
        lvl = normalize_level(row.get("interaction_level",""))
        counts[lvl] += 1
    return counts

def summarize_weighted(data):
    weighted = collections.Counter()
    for row in data:
        lvl = normalize_level(row.get("interaction_level",""))
        weight = WEIGHTS.get(lvl, 0.0)
        weighted[lvl] += weight
    return weighted

def export_json(obj, path="interaction_summary.json"):
    # convert Counter to plain dict with numeric values
    d = {k: (float(v) if isinstance(v, float) else int(v)) for k,v in obj.items()}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2)
    return path

def plot_summary_counter(counter_obj, path="interaction_summary_weighted.png", title="Weighted Interaction Summary"):
    keys = list(counter_obj.keys())
    vals = [counter_obj[k] for k in keys]
    plt.figure(figsize=(6,4))
    plt.bar(keys, vals, color="steelblue", edgecolor="black")
    plt.title(title)
    plt.xlabel("Interaction Level")
    plt.ylabel("Weighted Value")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path

if __name__ == "__main__":
    if not os.path.exists(CSV_PATH):
        print("ERROR: CSV not found:", CSV_PATH)
        raise SystemExit(1)

    data = load_data(CSV_PATH)

    counts = summarize_counts(data)
    weighted = summarize_weighted(data)

    print("Raw counts:", counts)
    print("Weighted totals:", weighted)

    # export both: counts (raw) and weighted
    export_json(counts, path="interaction_counts.json")
    export_json(weighted, path="interaction_weighted.json")

    # create two charts: raw counts + weighted totals
    plot_summary_counter(counts, path="interaction_counts.png", title="Interaction Counts (raw)")
    plot_summary_counter(weighted, path="interaction_weighted.png", title="Interaction Summary (weighted)")

    print("Exported: interaction_counts.json, interaction_weighted.json")
    print("Exported charts: interaction_counts.png, interaction_weighted.png")
