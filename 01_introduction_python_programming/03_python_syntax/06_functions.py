"""
Functions in Python
===================

What are functions?
-------------------
Functions are reusable blocks of code that perform a specific task. Think of
them as recipes - once you write the recipe (function), you can use it as many
times as you want with different ingredients (parameters).

Why do we need functions in pharmacy?
-------------------------------------
Pharmacists use the same calculations repeatedly:
- Calculating dosages based on weight (mg/kg)
- Converting units (mg to g, mL to L)
- Computing creatinine clearance for renal function
- Determining body surface area for chemotherapy

Instead of writing the same calculation code over and over, we write a function
once and reuse it with different values.

Function syntax:
    def function_name(parameter1, parameter2):
        # code that does something
        return result

Practical Example: Creating reusable drug calculation functions
"""

print("Pharmacy Calculation Functions\n")

# Example 1: Basic function without parameters
def display_pharmacy_header():
    return "*** Community Pharmacy System - Medication Dosage Calculator ***"

print(f"Ex1: {display_pharmacy_header()}\n")

# Example 2: Function with parameters and return value
def calculate_weight_based_dose(weight_kg, dose_per_kg):
    """Calculate drug dose based on patient weight."""
    return weight_kg * dose_per_kg

drug_dose_rate = 15.0
dose1 = calculate_weight_based_dose(70.0, drug_dose_rate)
dose2 = calculate_weight_based_dose(85.5, drug_dose_rate)
print(f"Ex2: Weight-based dosing at {drug_dose_rate} mg/kg")
print(f"  70.0 kg → {dose1} mg | 85.5 kg → {dose2} mg\n")

# Example 3: Function with multiple parameters
def calculate_adjusted_dose(weight_kg, standard_dose, age):
    """Calculate age-adjusted drug dose."""
    weight_adjusted = (weight_kg / 70.0) * standard_dose
    return weight_adjusted * 0.75 if age >= 65 else weight_adjusted

drug_name = "Warfarin"
standard_dose_mg = 5.0
adult_dose = calculate_adjusted_dose(75.0, standard_dose_mg, 45)
elderly_dose = calculate_adjusted_dose(68.0, standard_dose_mg, 72)
print(f"Ex3: {drug_name} (standard {standard_dose_mg} mg)")
print(f"  Adult (75kg, 45y): {adult_dose:.2f} mg | Elderly (68kg, 72y): {elderly_dose:.2f} mg\n")

# Example 4: Function returning multiple values
def calculate_dosing_schedule(single_dose, doses_per_day):
    """Calculate daily and weekly total doses."""
    daily_total = single_dose * doses_per_day
    weekly_total = daily_total * 7
    return daily_total, weekly_total

daily, weekly = calculate_dosing_schedule(500.0, 2)
print(f"Ex4: Metformin 500mg twice daily → Daily: {daily} mg, Weekly: {weekly} mg\n")

# Example 5: Creatinine clearance calculation (Cockcroft-Gault)
def calculate_creatinine_clearance(age, weight_kg, serum_creatinine, is_female):
    """Calculate creatinine clearance using Cockcroft-Gault formula."""
    clearance = ((140 - age) * weight_kg) / (72 * serum_creatinine)
    return clearance * 0.85 if is_female else clearance

crcl_a = calculate_creatinine_clearance(65, 80.0, 1.2, False)
crcl_b = calculate_creatinine_clearance(72, 65.0, 1.4, True)
print("Ex5: Renal function")
print(f"  John (M, 65y, 80kg, SCr 1.2): {crcl_a:.1f} mL/min")
print(f"  Mary (F, 72y, 65kg, SCr 1.4): {crcl_b:.1f} mL/min")

print(f"  → {'Dose adjustment needed' if crcl_b < 50 else 'Standard dosing OK'}")

print("\n✓ Functions enable code reuse with different parameters, improving organization and reducing errors.")
