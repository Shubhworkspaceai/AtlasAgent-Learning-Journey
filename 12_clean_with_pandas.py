#!/usr/bin/env python3
import pandas as pd
import re, json, os

IN = "data/drug_interactions.csv"
OUT = "data/clean_interactions.csv"
DRUGS_OUT = "data/unique_drugs.txt"

def norm_text(s):
    if pd.isna(s): return ""
    s = re.sub(r'[^\x20-\x7E]', '', str(s)).strip().lower()
    return re.sub(r'\s+', ' ', s)

def normalize_level(v):
    v = norm_text(v)
    if v in ('', 'na', 'n/a', 'none', 'no interaction'): return 'None'
    if v in ('high','h','severe'): return 'High'
    if v in ('moderate','med','m'): return 'Moderate'
    return v.capitalize()

def canonicalize_drug(name):
    s = norm_text(name)
    # small heuristics — extend later with real mapping
    s = s.replace('.', '')
    s = s.replace('-', ' ')
    return s.title()

if not os.path.exists(IN):
    raise SystemExit(f"Missing input CSV: {IN}")

df = pd.read_csv(IN)
expected = ['drug_a','drug_b','interaction_level','evidence','notes']
for c in expected:
    if c not in df.columns:
        df[c] = ''

df['drug_a_clean'] = df['drug_a'].apply(canonicalize_drug)
df['drug_b_clean'] = df['drug_b'].apply(canonicalize_drug)
df['interaction_level_clean'] = df['interaction_level'].apply(normalize_level)
df.to_csv(OUT, index=False)

drugs = sorted(set(df['drug_a_clean'].dropna().unique()) | set(df['drug_b_clean'].dropna().unique()))
with open(DRUGS_OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(drugs))

print(f"Saved cleaned CSV -> {OUT}")
print(f"Unique drugs list -> {DRUGS_OUT} ({len(drugs)} drugs)")
