"""
String Operations in Python
===========================

What are string operations?
---------------------------
Strings are sequences of characters (text). Python provides many useful methods
to manipulate and process text data.

Why are string operations important?
------------------------------------
In pharmacy systems, we often need to:
- Format patient names correctly (uppercase, lowercase, title case)
- Process drug information from text files
- Split combined data into separate parts
- Search for specific characters or patterns in text

String operations help us clean, format, and analyze text data efficiently.

Practical Example: Processing patient and drug information
"""

# Creating strings with quotes
drug_name = "acetylsalicylic acid"
patient_name = "john doe"
prescription_data = "Amoxicillin,500mg,twice daily,7 days"

print("Pharmacy Data Processing\n")

# String methods for formatting
print(f"'{drug_name}' → capitalize(): '{drug_name.capitalize()}' | upper(): '{drug_name.upper()}' | title(): '{drug_name.title()}'")
print(f"'{patient_name}' → title(): '{patient_name.title()}'\n")

# String concatenation using f-strings
patient_first = "Sarah"
patient_last = "Johnson"
patient_age = 45
drug_prescribed = "Metformin"
dosage = "850mg"

full_name = f"{patient_first} {patient_last}"
prescription_line = f"Patient: {full_name}, Age: {patient_age}, Prescribed: {drug_prescribed} {dosage}"
print(f"F-string concatenation: {prescription_line}\n")

# Using split() to separate data
prescription_parts = prescription_data.split(",")
print(f"split(',') on '{prescription_data}':\n  Drug: {prescription_parts[0]}, Dose: {prescription_parts[1]}, Frequency: {prescription_parts[2]}, Duration: {prescription_parts[3]}\n")

drug_full_name = "Acetaminophen Extra Strength Tablets"
words = drug_full_name.split(" ")
print(f"split(' ') on '{drug_full_name}': {words} ({len(words)} words)\n")

# Using replace() to standardize drug names
drug_variant1 = "Paracetamol"
standardized = drug_variant1.replace("Paracetamol", "Acetaminophen")
print(f"replace(): '{drug_variant1}' → '{standardized}'\n")

# Using count() to analyze text
chemical_formula = "C8H9NO2"
instruction = "Take one tablet twice daily with food and water"

print(f"count() on '{chemical_formula}': C={chemical_formula.count('C')}, H={chemical_formula.count('H')}")
print(f"count() on instruction: 'tablet'={instruction.count('tablet')}, 'daily'={instruction.count('daily')}")
print(f"'in' operator: 'food' in instruction = {'food' in instruction}, 'water' in instruction = {'water' in instruction}")

print("\n✓ String methods: split(), replace(), count(), and 'in' operator for text processing.")
