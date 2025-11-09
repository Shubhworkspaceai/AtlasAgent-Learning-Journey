print("===BODY MASS INDEX (BMI) CALCULATOR")
weight_kg = float(input("Enter your weight in kilograms: "))
height_input = float(input("Enter your height in meters (e.g.,1.75 for meters or 175 for cm): "))
# auto-detect if user typed centimeters instead of meters
if height_input > 10:  # assume value >10 means centimeters
    height_m = height_input / 100
else:
    height_m = height_input

bmi = weight_kg/ (height_m **2)
print(f"\nHeight interpreted as: {height_m:.2f} meters")
print(f"Your BMI is : {bmi: .2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
