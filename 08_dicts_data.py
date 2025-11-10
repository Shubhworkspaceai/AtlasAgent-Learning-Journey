# --- Day2 Step2: Dictionaries ---

drug_info = {
    "Aspirin": {"category": "NSAID", "max_dose": 4000},
    "Ibuprofen": {"category": "NSAID", "max_dose": 1200},
    "Warfarin": {"category": "Anticoagulant", "max_dose": 10},
}

print("Known drugs:", list(drug_info.keys()))

for name, data in drug_info.items():
    print(f"{name} ({data['category']}): Max {data['max_dose']} mg/day")

# add new record
drug_info["Paracetamol"] = {"category": "Analgesic", "max_dose": 4000}

# simple query
search = "Warfarin"
print(f"{search} class:", drug_info[search]["category"])
