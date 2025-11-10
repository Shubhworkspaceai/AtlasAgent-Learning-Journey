# --- Day2 Step5: Analyzer v2 ---
import csv, collections, matplotlib.pyplot as plt, json

CSV_PATH = "data/drug_interactions.csv"

def load_data(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def summarize(data):
    counts = collections.Counter(row["interaction_level"].capitalize() for row in data)
    return counts

def export_json(summary, path="interaction_summary.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    return path

def plot_summary(summary):
    plt.bar(summary.keys(), summary.values(), color="steelblue")
    plt.title("Drug Interaction Summary")
    plt.xlabel("Level")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("interaction_summary.png")
    plt.close()

if __name__ == "__main__":
    data = load_data(CSV_PATH)
    summary = summarize(data)
    print("Summary:", summary)
    export_json(summary)
    plot_summary(summary)
    print("Summary exported → interaction_summary.json")
    print("Chart exported → interaction_summary.png")
