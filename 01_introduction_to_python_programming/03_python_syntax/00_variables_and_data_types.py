"""
Variables and Data Types in Python
===================================

What are variables?
-------------------
Variables are containers that store data values. Think of them as labeled boxes
where you can store information and retrieve it later by using the label (variable name).

Why do we need variables?
-------------------------
In pharmacy calculations, we often need to store and reuse values like drug doses,
patient weights, or drug names. Variables let us store these values once and use
them multiple times in our calculations.

Three main data types:
----------------------
1. Integers (int): Whole numbers without decimals (e.g., patient age: 45)
2. Floats (float): Numbers with decimal points (e.g., drug concentration: 2.5)
3. Strings (str): Text enclosed in quotes (e.g., drug name: "Paracetamol")

Practical Example: Calculating drug dosages for different patients
"""

# String variable: Store the drug name
drug_name = "Paracetamol"

# Float variable: Store the recommended dose per kilogram of body weight (mg/kg)
dose_per_kg = 15.0

# Integer variable: Store a patient's age
patient_age = 35

print("Drug Dosage Calculator")
print(f"\nDrug: {drug_name} | Dose: {dose_per_kg} mg/kg\n")

# Patient 1: Calculate dosage for a 70 kg patient
patient_weight = 70.0
patient_dose = dose_per_kg * patient_weight
print(f"Patient 1: Age {patient_age} years, Weight {patient_weight} kg → Dose: {patient_dose} mg")

# Variables can be reassigned with new values
# Patient 2: Calculate dosage for a different patient
patient_age = 62
patient_weight = 85.5
patient_dose = dose_per_kg * patient_weight
print(f"Patient 2: Age {patient_age} years, Weight {patient_weight} kg → Dose: {patient_dose} mg")

# Patient 3: Pediatric patient with different weight
patient_age = 8
patient_weight = 25.0
patient_dose = dose_per_kg * patient_weight
print(f"Patient 3: Age {patient_age} years, Weight {patient_weight} kg → Dose: {patient_dose} mg")

print("\n✓ Variables store data that can be used in calculations and reassigned with new values.")
