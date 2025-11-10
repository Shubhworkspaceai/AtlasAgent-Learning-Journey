# --- Day2 Step1: Lists and Loops ---

drugs = ["Aspirin", "Ibuprofen", "Warfarin", "Paracetamol"]
print("Total drugs:", len(drugs))

# iterate with for loop
for drug in drugs:
    print(f"- {drug}")

# create a numeric list and compute mean manually
dosages = [100, 200, 300, 400]
avg_dose = sum(dosages) / len(dosages)
print(f"Average dosage: {avg_dose} mg")

# enumerate for index + value
for idx, drug in enumerate(drugs, start=1):
    print(f"{idx}. {drug}")
