"""
Conditional Statements (if/elif/else) in Python
===============================================

What are conditional statements?
---------------------------------
Conditional statements allow programs to make decisions and execute different
code based on whether conditions are true or false. Think of them as decision
points in your program.

Why do we need conditionals in pharmacy?
----------------------------------------
Pharmacists constantly make decisions based on conditions:
- Adjusting dosages based on patient age (pediatric vs adult vs geriatric)
- Checking if a drug interaction exists
- Determining if a patient is allergic to a medication
- Deciding if a refill is too early

Comparison operators:
- == (equal to)
- != (not equal to)
- < (less than)
- > (greater than)
- <= (less than or equal to)
- >= (greater than or equal to)

Practical Example: Determining appropriate drug dosages
"""

print("Drug Dosage Decision System\n")

# Example 1: Simple if/else
patient_name = "Emma Thompson"
patient_age = 8
drug_name = "Ibuprofen"

if patient_age >= 18:
    dosage = "400mg"
    category = "adult (18+)"
else:
    dosage = "200mg"
    category = "child (under 18)"

print(f"Ex1: {patient_name} ({patient_age}y, {drug_name}) → {category} → {dosage}\n")

# Example 2: if/elif/else chain
patient_name = "Michael Chen"
patient_age = 65
patient_weight = 75.0
drug_name = "Paracetamol"

if patient_age < 12:
    dosage = "250mg"
    category = "Pediatric"
elif patient_age < 18:
    dosage = "500mg"
    category = "Adolescent"
elif patient_age < 65:
    dosage = "1000mg"
    category = "Adult"
else:
    dosage = "500mg"
    category = "Geriatric (reduced)"

print(f"Ex2: {patient_name} ({patient_age}y, {patient_weight}kg, {drug_name}) → {category} → {dosage} every 6h\n")

# Example 3: Nested conditions
patient_name = "Sofia Rodriguez"
patient_age = 35
patient_weight = 48.0
drug_name = "Enoxaparin"

if patient_age < 18:
    result = "⚠ Pediatric - specialist consultation required"
else:
    if patient_weight < 50:
        dosage = "40mg"
    elif patient_weight <= 100:
        dosage = "60mg"
    else:
        dosage = "80mg"
    result = f"{dosage} once daily"

print(f"Ex3: {patient_name} ({patient_age}y, {patient_weight}kg, {drug_name}) → {result}\n")

# Example 4: Multiple conditions with 'and' operator
patient_name = "Robert Johnson"
patient_age = 72
creatinine_clearance = 35
drug_name = "Metformin"

if patient_age >= 65 and creatinine_clearance < 45:
    result = "⚠ CAUTION: Elderly with reduced kidney function → 500mg once daily"
elif creatinine_clearance < 30:
    result = "⚠ WARNING: Severe renal impairment → DO NOT PRESCRIBE"
else:
    result = "✓ Normal kidney function → 1000mg twice daily"

print(f"Ex4: {patient_name} ({patient_age}y, CrCl {creatinine_clearance} mL/min, {drug_name}) → {result}")

print("\n✓ Conditionals (if/elif/else) enable decision-making for appropriate dosing and safety.")
