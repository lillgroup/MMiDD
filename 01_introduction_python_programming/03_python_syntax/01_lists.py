"""
Lists in Python
===============

What are lists?
---------------
Lists are containers that can store multiple values in a single variable.
Think of a list as a collection of items stored in a specific order.

When do we use lists?
---------------------
In pharmacy, we often need to manage collections of items like:
- Multiple drug names in an inventory
- A patient's list of medications
- Expiration dates for different batches

Lists are created using square brackets [] with items separated by commas.

Practical Example: Managing a pharmacy medication inventory
"""

# Creating a list of drug names in our inventory
drug_inventory = ["Aspirin", "Ibuprofen", "Paracetamol", "Amoxicillin"]

print("Pharmacy Inventory Management\n")

# Display the complete inventory and demonstrate indexing
print(f"Current inventory: {drug_inventory} ({len(drug_inventory)} items)")
print(f"First: {drug_inventory[0]} | Last: {drug_inventory[-1]}")
print(f"First two: {drug_inventory[0:2]} | Last two: {drug_inventory[-2:]}\n")

# Adding a new medication to the inventory using append()
drug_inventory.append("Metformin")
print(f"After append('Metformin'): {drug_inventory} ({len(drug_inventory)} items)\n")

# Sorting the inventory alphabetically using sort()
drug_inventory.sort()
print(f"After sort(): {drug_inventory}\n")

# Removing medications using pop()
expired_drug = drug_inventory.pop()
print(f"After pop(): Removed '{expired_drug}' → {drug_inventory}")

removed_drug = drug_inventory.pop(1)
print(f"After pop(1): Removed '{removed_drug}' → {drug_inventory} ({len(drug_inventory)} items)")

print("\n✓ Lists store multiple items in order. Use indexing, slicing, append(), sort(), and pop().")
