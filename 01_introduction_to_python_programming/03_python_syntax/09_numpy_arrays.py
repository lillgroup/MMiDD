"""
NumPy Arrays for Scientific Computing
======================================

What is NumPy?
--------------
NumPy (Numerical Python) is the fundamental package for scientific computing
in Python. It provides powerful tools for working with arrays of numerical data.

Why use NumPy in molecular modeling?
------------------------------------
In drug design and molecular modeling, we work with large datasets:
- Molecular descriptors (logP, molecular weight, etc.)
- IC50 values for multiple compounds
- Coordinate data for molecular structures
- Large-scale calculations on many molecules

NumPy arrays are:
- Much faster than Python lists for numerical operations
- More memory-efficient for large datasets
- Designed for mathematical and scientific computations

Standard convention: import numpy as np

Practical Example: Analyzing molecular property data
"""

import numpy as np

print("NumPy Arrays for Molecular Data Analysis\n")

# Example 1: Creating arrays
print("Ex1: Creating NumPy arrays")

# Create array from a list - molecular weights in g/mol
molecular_weights = np.array([180.16, 294.74, 278.31, 342.30, 405.28])
print(f"Molecular weights: {molecular_weights}")
print(f"Type: {type(molecular_weights)}, Shape: {molecular_weights.shape}, Dtype: {molecular_weights.dtype}\n")

# Create array using np.arange() - compound IDs
compound_ids = np.arange(1, 11)  # Creates array [1, 2, 3, ..., 10]
print(f"Compound IDs: {compound_ids}\n")

# Example 2: Array indexing and slicing
print("Ex2: Array indexing and slicing")
logp_values = np.array([2.3, 3.5, 1.8, 4.2, 2.9, 3.1, 2.5, 3.8, 2.1, 4.0])

print(f"LogP values: {logp_values}")
print(f"First compound LogP: {logp_values[0]}")
print(f"Last compound LogP: {logp_values[-1]}")
print(f"First 3 compounds: {logp_values[0:3]}")
print(f"Compounds with LogP > 3.0: {logp_values[logp_values > 3.0]}\n")

# Example 3: Element-wise mathematical operations
print("Ex3: Mathematical operations on arrays")

# IC50 values in µM (micromolar)
ic50_values = np.array([5.2, 12.8, 3.4, 8.9, 15.3])
print(f"IC50 values (µM): {ic50_values}")

# Convert IC50 to pIC50: pIC50 = -log10(IC50 in M)
# First convert µM to M (divide by 1,000,000), then take -log10
ic50_in_molar = ic50_values / 1_000_000
pic50_values = -np.log10(ic50_in_molar)
print(f"pIC50 values: {pic50_values}")

# Calculate potency increase (multiply all IC50 by factor)
improved_ic50 = ic50_values / 2  # 2-fold improvement
print(f"Improved IC50 (2x better): {improved_ic50}\n")

# Example 4: Array statistics
print("Ex4: Statistical calculations")

binding_energies = np.array([-8.2, -7.5, -9.1, -6.8, -8.7, -7.9, -8.5, -9.3])
print(f"Binding energies (kcal/mol): {binding_energies}")
print(f"Mean: {binding_energies.mean():.2f} kcal/mol")
print(f"Std dev: {binding_energies.std():.2f} kcal/mol")
print(f"Min: {binding_energies.min():.2f} kcal/mol (best)")
print(f"Max: {binding_energies.max():.2f} kcal/mol (worst)")
print(f"Sum: {binding_energies.sum():.2f} kcal/mol\n")

# Example 5: Array reshaping
print("Ex5: Reshaping arrays for data organization")

# Flat array of molecular descriptors for 6 compounds: [MW, LogP, HBD, HBA]
descriptors = np.array([
    250.3, 2.5, 2, 3,  # Compound 1
    310.4, 3.8, 1, 4,  # Compound 2
    195.2, 1.9, 3, 2,  # Compound 3
    280.5, 3.2, 2, 3,  # Compound 4
    340.6, 4.1, 1, 5,  # Compound 5
    225.8, 2.8, 2, 4   # Compound 6
])

# Reshape to (6 compounds, 4 descriptors)
descriptors_matrix = descriptors.reshape(6, 4)
print("Descriptors matrix (6 compounds × 4 properties):")
print(descriptors_matrix)
print(f"\nCompound 1 descriptors: {descriptors_matrix[0]}")
print(f"All LogP values (column 1): {descriptors_matrix[:, 1]}")
print(f"Mean MW: {descriptors_matrix[:, 0].mean():.1f} g/mol\n")

# Example 6: Comparing NumPy efficiency
print("Ex6: NumPy vs Python lists - Efficiency demonstration")

# Python list approach
python_list = [1.5, 2.3, 3.7, 4.2, 5.1, 6.8, 7.3, 8.9, 9.2, 10.5]
list_sum = sum(python_list)
list_mean = list_sum / len(python_list)
print(f"Python list result: sum={list_sum:.1f}, mean={list_mean:.2f}")

# NumPy array approach (same data)
numpy_array = np.array(python_list)
numpy_sum = numpy_array.sum()
numpy_mean = numpy_array.mean()
print(f"NumPy array result: sum={numpy_sum:.1f}, mean={numpy_mean:.2f}")
print("→ Same results, but NumPy is much faster for large datasets!\n")

# Example 7: Practical application - Drug-likeness filtering
print("Ex7: Drug-likeness screening (Lipinski's Rule of 5)")

# Molecular descriptors for 5 compounds
compounds = np.array([
    [280.3, 2.5, 2, 4],  # MW, LogP, HBD, HBA - Compound A
    [520.8, 5.8, 0, 8],  # Compound B (violates rules)
    [195.2, 1.9, 3, 2],  # Compound C
    [310.4, 3.2, 1, 5],  # Compound D
    [680.5, 6.5, 1, 12]  # Compound E (violates rules)
])

# Lipinski's Rule of 5: MW ≤ 500, LogP ≤ 5, HBD ≤ 5, HBA ≤ 10
lipinski_pass = (
    (compounds[:, 0] <= 500) &  # MW
    (compounds[:, 1] <= 5) &     # LogP
    (compounds[:, 2] <= 5) &     # HBD
    (compounds[:, 3] <= 10)      # HBA
)

print("Compound screening results:")
for i, passes in enumerate(lipinski_pass):
    status = "✓ PASS" if passes else "✗ FAIL"
    print(f"  Compound {chr(65+i)}: MW={compounds[i,0]:.1f}, LogP={compounds[i,1]:.1f} → {status}")

print(f"\nPassing compounds: {lipinski_pass.sum()} out of {len(lipinski_pass)}")

print("\n✓ NumPy arrays: efficient numerical computing for molecular data analysis.")
