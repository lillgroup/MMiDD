"""
Dictionaries in Python
======================

What are dictionaries?
----------------------
Dictionaries are containers that store data in key-value pairs. Think of them
as labeled storage boxes where each piece of data has a unique label (key)
that you use to access the value.

Why use dictionaries?
---------------------
In pharmacy, we often need to store related information together:
- A drug with its name, dosage, price, and manufacturer
- A patient with their name, age, allergies, and medications

Dictionaries let us organize this structured data in a clear, accessible way.

Dictionaries are created using curly braces {} with key: value pairs.

Practical Example: Storing and managing drug information
"""

# Creating a dictionary to store information about a drug
drug_info = {
    "name": "Amoxicillin",
    "dosage": "500mg",
    "price": 12.50,
    "manufacturer": "PharmaCorp"
}

print("Drug Information Management\n")
print(f"Initial: {drug_info}\n")

# Accessing values using keys
print(f"Accessing: {drug_info['name']}, {drug_info['dosage']}, ${drug_info['price']}, {drug_info['manufacturer']}\n")

# Adding a new key-value pair and modifying an existing value
drug_info["expiration_date"] = "2026-12-31"
drug_info["price"] = 10.75
print(f"After adding expiration_date and updating price: {drug_info}\n")

# Creating another dictionary for a different drug
second_drug = {
    "name": "Ibuprofen",
    "dosage": "200mg",
    "price": 8.25,
    "manufacturer": "HealthMeds",
    "expiration_date": "2027-03-15"
}

print(f"Second drug: {second_drug}\n")

# Comparing prices
price_difference = drug_info['price'] - second_drug['price']
print(f"Price comparison: {drug_info['name']} (${drug_info['price']}) vs {second_drug['name']} (${second_drug['price']})")
print(f"Difference: ${price_difference:.2f}")

print("\n✓ Dictionaries store data in key-value pairs for organized, accessible information.")
