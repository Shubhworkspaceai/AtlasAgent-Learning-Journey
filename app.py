import streamlit as st
import csv, os

DB_PATH = os.path.join('data', 'drug_interactions.csv')

def load_db(path):
    db = {}
    if not os.path.exists(path):
        return db
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            a = row['drug_a'].strip().lower()
            b = row['drug_b'].strip().lower()
            key = tuple(sorted([a,b]))
            db[key] = {
                'level': row.get('interaction_level','none'),
                'evidence': row.get('evidence',''),
                'notes': row.get('notes','')
            }
    return db

def find_interaction(drug1, drug2, db):
    a = drug1.strip().lower()
    b = drug2.strip().lower()
    key = tuple(sorted([a,b]))
    return db.get(key, {'level':'none','evidence':'','notes':''})

st.set_page_config(page_title="AtlasAgent — Interaction Checker", layout="centered")
st.title("AtlasAgent — Drug Interaction Checker (Demo)")

db = load_db(DB_PATH)
all_drugs = set()
for k in db.keys():
    all_drugs.update(k)
all_drugs = sorted(list(all_drugs))

col1, col2 = st.columns(2)
with col1:
    drug1 = st.selectbox("Select drug 1", options=[""] + all_drugs)
with col2:
    drug2 = st.selectbox("Select drug 2", options=[""] + all_drugs)

if st.button("Check Interaction"):
    if not drug1 or not drug2:
        st.error("Please select both drugs.")
    elif drug1 == drug2:
        st.warning("Same drug selected — no pairwise interaction to check.")
    else:
        res = find_interaction(drug1, drug2, db)
        level = res.get('level','none')
        evidence = res.get('evidence','').strip()
        notes = res.get('notes','').strip()

        if level.lower() == 'high':
            st.error("⚠️ HIGH interaction risk detected.")
        elif level.lower() == 'moderate':
            st.warning("⚠️ Moderate interaction risk detected.")
        elif level.lower() == 'none' or level=='':
            st.success("✅ No known interaction in local DB.")
        else:
            st.info(f"Interaction level: {level}")

        if evidence:
            st.markdown(f"**Evidence:** {evidence}")
        if notes:
            st.markdown(f"**Notes:** {notes}")

st.markdown("---")
st.caption("This is a demo. Not clinical advice. See code for details.")
