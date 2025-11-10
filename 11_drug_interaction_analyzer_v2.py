# --- Day2 Step5: Analyzer v2 ---
import csv, collections, matplotlib.pyplot as plt, json, os

CSV_PATH = "data/drug_interactions.csv"

def load_data(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def summarize(data):
    counts = collections.Counter((row.get("interaction_level") or "none").strip().capitalize() for row in data)
    return counts

def export_json(summary, path="interaction_summary.json"):
    obj = {k: int(v) for k,v in summary.items()}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
    return path

def plot_summary(summary, path="interaction_summary.png"):
    keys = list(summary.keys())
    vals = [int(summary[k]) for k in keys]
    plt.figure(figsize=(6,4))
    plt.bar(keys, vals)
    plt.title("Drug Interaction Summary")
    plt.xlabel("Interaction Level")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path

if __name__ == "__main__":
    if not os.path.exists(CSV_PATH):
        print("ERROR: CSV not found:", CSV_PATH)
        raise SystemExit(1)
    data = load_data(CSV_PATH)
    summary = summarize(data)
    print("Summary (counts):", summary)
    json_path = export_json(summary)
    png_path = plot_summary(summary)
    print("Exported JSON ->", json_path)
    print("Exported chart ->", png_path)
