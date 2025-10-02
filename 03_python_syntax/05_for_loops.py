"""
For Loops in Python
===================

What are loops?
---------------
Loops allow us to execute the same code multiple times without writing it
repeatedly. Think of a loop as automating repetitive tasks.

Why do we need loops in pharmacy?
---------------------------------
Pharmacists often need to perform the same task for multiple items:
- Calculate dosages for multiple patients
- Process a list of medications in inventory
- Check expiration dates for all drugs
- Generate labels for multiple prescriptions

Instead of writing the same code over and over, we use loops to do it efficiently.

The for loop syntax:
    for item in list:
        # code to execute for each item

Practical Example: Processing patient dosages and medication inventory
"""

print("Pharmacy Batch Processing System\n")

# Example 1: Basic for loop
drug_name = "Enoxaparin"
dose_per_kg = 1.5
patient_weights = [65.0, 78.5, 52.0, 90.0, 58.5]

print(f"Ex1: {drug_name} at {dose_per_kg} mg/kg")
for weight in patient_weights:
    print(f"  {weight} kg → {dose_per_kg * weight} mg")

print("\nEx2: Inventory with enumerate()")
medications = ["Aspirin", "Metformin", "Lisinopril", "Atorvastatin", "Omeprazole"]
for index, medication in enumerate(medications):
    print(f"  Item {index + 1}: {medication}")

print("\nEx3: Multiple patients")
patients = ["Alice Johnson", "Bob Smith", "Carol Davis", "David Martinez"]
weights = [68.0, 85.0, 52.0, 74.5]
drug = "Amoxicillin"
dose_per_kg = 15.0

for index, patient_name in enumerate(patients):
    required_dose = dose_per_kg * weights[index]
    print(f"  {patient_name}: {weights[index]} kg → {required_dose} mg")

print("\nEx4: Expiration check")
medications_with_expiry = [
    ("Ibuprofen", 2026), ("Paracetamol", 2024), ("Aspirin", 2025),
    ("Cetirizine", 2024), ("Loratadine", 2027)
]
current_year = 2025

for medication, expiry_year in medications_with_expiry:
    if expiry_year < current_year:
        status = "⚠ EXPIRED"
    elif expiry_year == current_year:
        status = "⚠ EXPIRES THIS YEAR"
    else:
        status = "✓ Valid"
    print(f"  {medication} ({expiry_year}): {status}")

print("\nEx5: Inventory value")
drug_names_with_prices = ["Aspirin", "Ibuprofen", "Amoxicillin", "Metformin", "Lisinopril"]
drug_prices = [12.50, 8.75, 15.00, 22.50, 18.00]
total_value = 0.0

for index, drug in enumerate(drug_names_with_prices):
    price = drug_prices[index]
    total_value += price
    print(f"  {drug}: ${price:.2f}")

print(f"  Total: ${total_value:.2f}")

print("\n✓ For loops automate repetitive tasks. Use enumerate() for index+value.")
print("For loops allow us to process multiple items efficiently without")
print("repeating code. Use enumerate() to get both the position and value")
print("when you need to track item numbers or access parallel lists.")
print("=" * 60)
