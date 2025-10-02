"""
Pandas for Structured Data Analysis
====================================

What is Pandas?
---------------
Pandas is a powerful Python library for data manipulation and analysis.
It provides DataFrame objects that work like spreadsheets or database tables,
making it easy to organize, filter, and analyze structured data.

Why use Pandas in drug design?
------------------------------
In pharmaceutical research, we work with tabular data:
- Compound databases with multiple properties
- Experimental results (IC50, Ki, binding affinity)
- QSAR datasets with molecular descriptors
- Clinical trial data

Pandas makes it easy to:
- Load data from CSV, Excel, or databases
- Filter and select specific compounds
- Calculate statistics and summaries
- Combine and merge datasets

Standard convention: import pandas as pd

Practical Example: Analyzing drug compound databases
"""

import pandas as pd
import numpy as np

print("Pandas for Molecular Data Management\n")

# Example 1: Creating DataFrames from dictionaries
print("Ex1: Creating a DataFrame from drug data\n")

# Drug compound data
compounds = {
    'compound_id': ['CPD001', 'CPD002', 'CPD003', 'CPD004', 'CPD005'],
    'name': ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Metformin', 'Atorvastatin'],
    'molecular_weight': [180.16, 206.28, 151.16, 129.16, 558.64],
    'logp': [1.19, 3.97, 0.46, -1.43, 5.39],
    'ic50_um': [25.4, 15.2, 45.8, 8.5, 3.2]
}

df = pd.DataFrame(compounds)
print(df)
print()

# Example 2: Basic DataFrame operations
print("Ex2: DataFrame information and statistics\n")

print("First 3 rows:")
print(df.head(3))
print()

print("DataFrame info:")
print(df.info())
print()

print("Statistical summary:")
print(df.describe())
print()

# Example 3: Selecting columns and rows
print("Ex3: Selecting data\n")

# Select single column
print("Molecular weights:")
print(df['molecular_weight'])
print()

# Select multiple columns
print("Name and IC50 values:")
print(df[['name', 'ic50_um']])
print()

# Select specific rows by index
print("First compound (row 0):")
print(df.iloc[0])
print()

# Select by condition
print("Compounds with IC50 < 20 µM (potent):")
potent_compounds = df[df['ic50_um'] < 20]
print(potent_compounds[['name', 'ic50_um']])
print()

# Example 4: Reading data from CSV file
print("Ex4: Loading data from CSV file\n")

# Read the compounds CSV file
df_csv = pd.read_csv('compounds_data.csv')
print(f"Loaded {len(df_csv)} compounds from CSV")
print(df_csv.head())
print()

# Example 5: Data filtering and sorting
print("Ex5: Filtering and sorting operations\n")

# Filter by multiple conditions
drug_like = df_csv[
    (df_csv['molecular_weight'] <= 500) &
    (df_csv['logp'] <= 5) &
    (df_csv['ic50_um'] < 20)
]
print(f"Drug-like compounds (MW≤500, LogP≤5, IC50<20): {len(drug_like)} found")
print(drug_like[['name', 'molecular_weight', 'logp', 'ic50_um']])
print()

# Sort by IC50 (ascending - most potent first)
sorted_by_potency = df_csv.sort_values('ic50_um')
print("Top 5 most potent compounds (lowest IC50):")
print(sorted_by_potency[['name', 'ic50_um']].head())
print()

# Example 6: Adding calculated columns
print("Ex6: Adding new calculated columns\n")

# Calculate pIC50 from IC50
df_csv['pic50'] = -np.log10(df_csv['ic50_um'] / 1_000_000)

# Calculate ligand efficiency (LE = pIC50 / heavy atom count)
# Approximation: heavy atoms ≈ MW / 15
df_csv['heavy_atoms'] = (df_csv['molecular_weight'] / 15).round()
df_csv['ligand_efficiency'] = df_csv['pic50'] / df_csv['heavy_atoms']

print("DataFrame with calculated properties:")
print(df_csv[['name', 'ic50_um', 'pic50', 'ligand_efficiency']].head())
print()

# Example 7: Grouping and aggregation
print("Ex7: Data grouping and statistics\n")

# Group by solubility and calculate mean IC50
solubility_stats = df_csv.groupby('solubility')['ic50_um'].agg(['mean', 'count'])
print("IC50 statistics by solubility:")
print(solubility_stats)
print()

# Example 8: Basic data summary
print("Ex8: Quick data insights\n")

print(f"Total compounds: {len(df_csv)}")
print(f"Mean molecular weight: {df_csv['molecular_weight'].mean():.2f} g/mol")
print(f"Mean LogP: {df_csv['logp'].mean():.2f}")
print(f"Most potent compound: {df_csv.loc[df_csv['ic50_um'].idxmin(), 'name']} (IC50: {df_csv['ic50_um'].min():.1f} µM)")
print(f"Largest compound: {df_csv.loc[df_csv['molecular_weight'].idxmax(), 'name']} (MW: {df_csv['molecular_weight'].max():.2f} g/mol)")
print()

# Example 9: Exporting data
print("Ex9: Saving filtered data\n")

# Save drug-like compounds to a new CSV
drug_like.to_csv('drug_like_compounds.csv', index=False)
print("✓ Drug-like compounds saved to 'drug_like_compounds.csv'")

print("\n✓ Pandas DataFrames: essential for organizing and analyzing molecular data.")
