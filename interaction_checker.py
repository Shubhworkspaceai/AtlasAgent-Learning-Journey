#!/usr/bin/env python3
"""
05_interaction_checker.py
- Uses a small CSV "database" of known interactions.
- Case-insensitive, robust input, returns evidence and advice.
- Example usage: run and type two drug names.
"""

import csv
import os
from typing import Tuple, Dict, Optional

DB_PATH = os.path.join('data', 'drug_interactions.csv')

def load_interaction_db(path: str) -> Dict[Tuple[str,str], Dict]:
    db = {}
    if not os.path.exists(path):
        return db
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            a = row['drug_a'].strip().lower()
            b = row['drug_b'].strip().lower()
            key = tuple(sorted([a,b]))
            db[key] = {
                'level': row.get('interaction_level','unknown'),
                'evidence': row.get('evidence',''),
                'notes': row.get('notes','')
            }
    return db

def find_interaction(drug1: str, drug2: str, db: Dict) -> Dict:
    a = drug1.strip().lower()
    b = drug2.strip().lower()
    key = tuple(sorted([a,b]))
    return db.get(key, {'level':'none','evidence':'','notes':''})

def main():
    db = load_interaction_db(DB_PATH)
    print("=== Drug Interaction Checker v0.2 ===")
    d1 = input("Enter first drug: ").strip()
    d2 = input("Enter second drug: ").strip()

    if not d1 or not d2:
        print("Error: please enter both drug names.")
        return

    result = find_interaction(d1, d2, db)
    level = result['level']
    evidence = result.get('evidence','').strip()
    notes = result.get('notes','').strip()

    if level in ('high','High','HIGH'):
        print("⚠️ DANGER: HIGH interaction risk detected.")
    elif level in ('moderate','Moderate'):
        print("⚠️ WARNING: Moderate interaction risk detected.")
    elif level == 'none':
        print("✅ No known interaction in local DB.")
    else:
        print("ℹ️ Interaction level:", level)

    if evidence:
        print("Evidence:", evidence)
    if notes:
        print("Notes:", notes)

if __name__=='__main__':
    main()
