"""
Importing Modules in Python
============================

What are modules?
-----------------
Modules are pre-written Python code libraries that provide additional functions
and capabilities. Think of them as toolboxes containing specialized tools that
we can use in our programs.

Why do we need modules in pharmacy?
-----------------------------------
Many pharmaceutical calculations require advanced mathematical functions:
- Square roots for dose calculations
- Exponential functions for drug decay and pharmacokinetics
- Logarithms for pH calculations
- Trigonometric functions for certain formulas

The 'math' module provides these mathematical functions.

Importing syntax:
    import math
    
Then use: math.function_name()

Practical Example: Pharmaceutical calculations using the math module
"""

# Import the math module
import math

print("Pharmaceutical Calculations with Math Module\n")

# Example 1: Body Surface Area using math.sqrt()
height_cm = 165.0
weight_kg = 68.0
bsa = math.sqrt((height_cm * weight_kg) / 3600)
drug_name = "Doxorubicin"
dose_per_m2 = 60
total_dose = bsa * dose_per_m2
print(f"Ex1: BSA = sqrt({height_cm} x {weight_kg}/3600) = {bsa:.2f} m² → {drug_name} dose: {total_dose:.2f} mg\n")

# Example 2: Drug elimination using math.exp()
drug = "Theophylline"
initial_concentration = 20.0
elimination_constant = 0.1
time_points = [0, 2, 4, 6, 8, 12]

print(f"Ex2: {drug} concentration over time (C₀={initial_concentration} mg/L, k={elimination_constant}/h)")
for time_hours in time_points:
    concentration = initial_concentration * math.exp(-elimination_constant * time_hours)
    print(f"  {time_hours}h: {concentration:.2f} mg/L")
print()

# Example 3: Half-life using math.log()
drug_name = "Digoxin"
k_elimination = 0.015
half_life_hours = math.log(2) / k_elimination
print(f"Ex3: {drug_name} half-life = ln(2)/{k_elimination} = {half_life_hours:.1f}h ({half_life_hours/24:.1f} days)\n")

# Example 4: Loading dose
target_concentration = 15.0
volume_distribution = 0.7
patient_weight = 75.0
bioavailability = 0.85
total_volume = volume_distribution * patient_weight
loading_dose = (target_concentration * total_volume) / bioavailability
print(f"Ex4: Loading dose = ({target_concentration}x{total_volume:.1f})/{bioavailability} = {loading_dose:.1f} mg\n")

# Example 5: Drip rate using math.ceil()
volume_ml = 1000
infusion_time_hours = 8
drop_factor = 15
infusion_time_minutes = infusion_time_hours * 60
drip_rate = (volume_ml * drop_factor) / infusion_time_minutes
drip_rate_rounded = math.ceil(drip_rate)
print(f"Ex5: IV drip rate = {drip_rate:.2f} drops/min → ceil() = {drip_rate_rounded} drops/min\n")

# Example 6: Using math.pi constant
cylinder_radius = 3.5
cylinder_height = 12.0
volume_cubic_cm = math.pi * math.pow(cylinder_radius, 2) * cylinder_height
print(f"Ex6: Cylinder volume = π x r² x h = {math.pi:.4f}x{cylinder_radius}² x {cylinder_height} = {volume_cubic_cm:.2f} cm³\n")

# Example 7: pH using math.log10()
h_concentration = 0.0001
ph_value = -math.log10(h_concentration)
classification = "Acidic" if ph_value < 7 else ("Neutral" if ph_value == 7 else "Basic")
print(f"Ex7: pH = -log₁₀[{h_concentration}] = {ph_value:.2f} ({classification})")

print("\n✓ Math module: sqrt(), exp(), log(), log10(), pow(), ceil(), and constants like pi.")
