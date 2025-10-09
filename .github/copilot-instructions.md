# GitHub Copilot Code Generation Instructions for Students

## Overview

These instructions ensure that GitHub Copilot generates code that aligns with the Python concepts students have learned in this course. Code suggestions should only use patterns, syntax, and libraries that students have been explicitly taught.

---

## Allowed Python Concepts

### 1. Variables and Data Types

**ALLOWED:**
- Basic data types: `int`, `float`, `str`
- Variable assignment and reassignment
- Arithmetic operations: `+`, `-`, `*`, `/`, `**` (exponentiation)
- f-strings for string formatting: `f"Text {variable}"`
- Type conversion: `int()`, `float()`, `str()`

**Example:**
```python
drug_name = "Paracetamol"
dose_per_kg = 15.0
patient_weight = 70.0
patient_dose = dose_per_kg * patient_weight
print(f"Patient dose: {patient_dose} mg")
```

---

### 2. Lists

**ALLOWED:**
- Creating lists with square brackets: `[]`
- Accessing elements by index: `list[0]`, `list[-1]`
- Slicing: `list[0:2]`, `list[-2:]`
- Built-in function: `len()`
- Methods: `append()`, `sort()`, `pop()`, `pop(index)`

**NOT ALLOWED:**
- List comprehensions
- Methods: `extend()`, `insert()`, `remove()`, `clear()`, `reverse()`, `copy()`, `count()`, `index()`
- Advanced operations like `zip()`, `map()`, `filter()`

**Example:**
```python
drug_inventory = ["Aspirin", "Ibuprofen", "Paracetamol"]
drug_inventory.append("Metformin")
drug_inventory.sort()
removed = drug_inventory.pop()
```

---

### 3. Dictionaries

**ALLOWED:**
- Creating dictionaries with curly braces: `{}`
- Key-value pairs: `{"key": value}`
- Accessing values: `dict["key"]`
- Adding new key-value pairs: `dict["new_key"] = value`
- Modifying existing values: `dict["key"] = new_value`

**NOT ALLOWED:**
- Dictionary methods: `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`, etc.
- Dictionary comprehensions
- Advanced operations

**Example:**
```python
drug_info = {
    "name": "Amoxicillin",
    "dosage": "500mg",
    "price": 12.50
}
print(drug_info["name"])
drug_info["price"] = 10.75
drug_info["expiration_date"] = "2026-12-31"
```

---

### 4. String Operations

**ALLOWED:**
- String methods: `capitalize()`, `upper()`, `lower()`, `title()`, `split()`, `replace()`, `count()`
- Membership operator: `in`
- String concatenation with f-strings: `f"{var1} {var2}"`
- Indexing and slicing strings

**NOT ALLOWED:**
- Advanced string methods: `join()`, `strip()` (except in file reading context), `startswith()`, `endswith()`, `find()`, `format()`, etc.
- Regular expressions
- String formatting with `%` or `.format()`

**Example:**
```python
drug_name = "acetylsalicylic acid"
print(drug_name.title())
patient_name = "john doe"
full_name = patient_name.title()
data = "Amoxicillin,500mg,twice daily"
parts = data.split(",")
```

---

### 5. Conditional Statements

**ALLOWED:**
- `if`, `elif`, `else` statements
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operator: `and` (only in simple combinations)
- Nested if statements (simple nesting only)

**NOT ALLOWED:**
- Logical operators: `or`, `not`
- Ternary operators: `x if condition else y`
- Complex boolean logic

**Example:**
```python
if patient_age >= 18:
    dosage = "400mg"
else:
    dosage = "200mg"

if patient_age < 12:
    dosage = "250mg"
elif patient_age < 18:
    dosage = "500mg"
else:
    dosage = "1000mg"

if patient_age >= 65 and creatinine_clearance < 45:
    result = "CAUTION: Reduced dose"
```

---

### 6. For Loops

**ALLOWED:**
- Basic for loops: `for item in list:`
- Using `enumerate()` for index and value: `for index, item in enumerate(list):`
- Iterating over lists
- Iterating over tuples in a list: `for item1, item2 in list_of_tuples:`
- Accumulator pattern (e.g., `total += value`)
- Using loop variable in calculations

**NOT ALLOWED:**
- `while` loops
- `range()` function
- `break` and `continue` statements
- Nested loops with complex logic
- `zip()` function for parallel iteration

**Example:**
```python
patient_weights = [65.0, 78.5, 52.0, 90.0]
for weight in patient_weights:
    dose = dose_per_kg * weight
    print(f"{weight} kg → {dose} mg")

for index, medication in enumerate(medications):
    print(f"Item {index + 1}: {medication}")

for drug, expiry_year in medications_with_expiry:
    if expiry_year < current_year:
        print(f"{drug}: EXPIRED")
```

---

### 7. Functions

**ALLOWED:**
- Function definition: `def function_name(parameters):`
- Parameters (positional only, no default values)
- Return statements: `return value` or `return value1, value2`
- Calling functions with arguments
- Docstrings (simple one-line descriptions)

**NOT ALLOWED:**
- Default parameter values
- Keyword arguments
- `*args` and `**kwargs`
- Lambda functions
- Decorators
- Recursive functions

**Example:**
```python
def calculate_weight_based_dose(weight_kg, dose_per_kg):
    """Calculate drug dose based on patient weight."""
    return weight_kg * dose_per_kg

def calculate_dosing_schedule(single_dose, doses_per_day):
    """Calculate daily and weekly total doses."""
    daily_total = single_dose * doses_per_day
    weekly_total = daily_total * 7
    return daily_total, weekly_total

dose = calculate_weight_based_dose(70.0, 15.0)
daily, weekly = calculate_dosing_schedule(500.0, 2)
```

---

### 8. File Reading

**ALLOWED:**
- Using `with open()` statement: `with open('filename.txt', 'r', encoding='utf-8') as file:`
- Reading entire file: `file.read()`
- Reading line by line: `for line in file:`
- String method `strip()` to remove whitespace (in file reading context only)
- Error handling with `try`/`except FileNotFoundError`
- Error handling with `try`/`except ValueError`
- Error handling with `try`/`except IndexError`
- Checking for empty lines: `if not line:`

**NOT ALLOWED:**
- File writing operations
- Other file modes: `'w'`, `'a'`, `'r+'`, etc.
- Methods: `readlines()`, `readline()`
- Context managers beyond basic file operations
- More complex exception handling

**Example:**
```python
try:
    with open('drug_inventory.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            drug_name = parts[0]
            price = float(parts[2])
            print(f"{drug_name}: ${price}")
except FileNotFoundError:
    print("Error: File not found!")
except ValueError:
    print("Error: Invalid data format!")
```

---

### 9. Math Module

**ALLOWED:**
- Import statement: `import math`
- Functions: `math.sqrt()`, `math.exp()`, `math.log()`, `math.log10()`, `math.pow()`, `math.ceil()`
- Constants: `math.pi`
- Using functions with dot notation: `math.function_name()`

**NOT ALLOWED:**
- Other math functions not explicitly listed
- `from math import ...` syntax
- Other modules unless explicitly listed below

**Example:**
```python
import math

bsa = math.sqrt((height_cm * weight_kg) / 3600)
concentration = initial * math.exp(-k * time)
half_life = math.log(2) / k_elimination
ph_value = -math.log10(h_concentration)
volume = math.pi * math.pow(radius, 2) * height
```

---

### 10. NumPy Arrays

**ALLOWED:**
- Import statement: `import numpy as np`
- Creating arrays: `np.array([list])`, `np.arange(start, stop)`
- Indexing and slicing: `array[0]`, `array[-1]`, `array[0:3]`, `array[:, 1]`
- Boolean indexing: `array[array > value]`
- Element-wise operations: `+`, `-`, `*`, `/` on arrays
- Mathematical functions: `np.log10()`, `np.exp()`
- Statistical methods: `.mean()`, `.std()`, `.min()`, `.max()`, `.sum()`
- Array reshaping: `.reshape(rows, cols)`
- Array attribute: `.shape`
- Creating sequences: `np.linspace()`, `np.logspace()`
- Random number generation: `np.random.seed()`, `np.random.lognormal()`

**NOT ALLOWED:**
- Advanced NumPy functions not listed above
- Matrix operations, linear algebra
- Advanced array manipulation beyond basic reshaping
- Broadcasting beyond simple element-wise operations

**Example:**
```python
import numpy as np

molecular_weights = np.array([180.16, 294.74, 278.31])
compound_ids = np.arange(1, 11)
logp_values = np.array([2.3, 3.5, 1.8, 4.2])
high_logp = logp_values[logp_values > 3.0]

ic50_in_molar = ic50_values / 1_000_000
pic50_values = -np.log10(ic50_in_molar)

mean_energy = binding_energies.mean()
std_energy = binding_energies.std()

descriptors_matrix = descriptors.reshape(6, 4)
```

---

### 11. Pandas DataFrames

**ALLOWED:**
- Import statement: `import pandas as pd`
- Creating DataFrames from dictionaries: `pd.DataFrame(dict)`
- Reading CSV files: `pd.read_csv('filename.csv')`
- Viewing data: `.head()`, `.head(n)`, `.info()`, `.describe()`
- Selecting columns: `df['column']`, `df[['col1', 'col2']]`
- Selecting rows by index: `.iloc[index]`
- Filtering with conditions: `df[df['column'] < value]`
- Multiple conditions with `&`: `df[(df['col1'] < val1) & (df['col2'] > val2)]`
- Sorting: `.sort_values('column')`
- Adding calculated columns: `df['new_col'] = calculation`
- Grouping: `.groupby('column')['other_column'].agg(['mean', 'count'])`
- Finding max/min locations: `.idxmin()`, `.idxmax()`
- Accessing values: `.loc[index, 'column']`
- Getting length: `len(df)`
- Saving to CSV: `.to_csv('filename.csv', index=False)`

**NOT ALLOWED:**
- Advanced indexing: `.at[]`, `.iat[]`
- Row selection: `.loc[]` with labels
- Methods: `.apply()`, `.map()`, `.merge()`, `.join()`, `.concat()`, `.pivot()`, `.melt()`, etc.
- Advanced aggregation beyond basic `.agg()`
- Multi-index operations

**Example:**
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Aspirin', 'Ibuprofen', 'Paracetamol'],
    'molecular_weight': [180.16, 206.28, 151.16],
    'ic50_um': [25.4, 15.2, 45.8]
})

print(df.head())
print(df.describe())

mw_values = df['molecular_weight']
potent = df[df['ic50_um'] < 20]
drug_like = df[(df['molecular_weight'] <= 500) & (df['ic50_um'] < 20)]

sorted_df = df.sort_values('ic50_um')
df['pic50'] = -np.log10(df['ic50_um'] / 1_000_000)

df_csv = pd.read_csv('compounds.csv')
df_csv.to_csv('filtered.csv', index=False)
```

---

### 12. Matplotlib Plotting

**ALLOWED:**

--- All plots must use the tab10 color palette from matplotlib for colors. For bar, scatter, pie, and other plots, use colors from `matplotlib.cm.get_cmap('tab10').colors` and assign colors consistently to categories or groups.

**NOT ALLOWED:**
- Advanced plot types not listed above
- 3D plotting
- Animations
- Interactive plots
- Customizing tick labels beyond basic usage
- Advanced subplot arrangements beyond simple grids
- Object-oriented API beyond basic subplots

**Example:**
```python
import matplotlib.pyplot as plt
import numpy as np

time = np.array([0, 0.5, 1, 2, 4, 6, 8, 12, 24])
concentration = np.array([0, 8.5, 12.3, 15.2, 13.8, 11.5, 9.2, 6.4, 2.1])

plt.figure(figsize=(8, 5))
plt.plot(time, concentration, marker='o', linewidth=2, color='blue')
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Concentration (µg/mL)', fontsize=12)
plt.title('Pharmacokinetic Profile', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.close()

# Subplots example
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Dashboard', fontsize=16, fontweight='bold')
axes[0, 0].bar(compounds, ic50_data, color='blue', alpha=0.7)
axes[0, 0].set_ylabel('IC50 (µM)')
axes[0, 0].set_title('Potency')
plt.tight_layout()
plt.savefig('dashboard.png', dpi=300, bbox_inches='tight')
```

---

## General Code Generation Rules

### Style and Formatting

1. **Comments**: ALWAYS include exhaustive, educational comments throughout the code
   - Place comments on the line BEFORE the code they describe
   - NEVER use inline comments
   - Explain WHAT the code does, WHY it's needed, and HOW it works
   - Write comments for EVERY line or logical block of code
   - Use beginner-friendly language - assume the reader is learning programming
   - Explain programming concepts explicitly (e.g., "Loop through each item", "Check if condition is true")
   - Reference pharmaceutical/scientific context to connect code to domain knowledge
   - For complex operations, break down the explanation into multiple comment lines
   - Think of comments as teaching tools, not just documentation

2. **Variable Names**: Use clear, descriptive names
   - Use snake_case for variables and functions
   - Avoid single-letter variables except in simple loops
   - Use meaningful pharmaceutical/scientific context

3. **Print Statements**: Use for displaying results and progress
   - Use f-strings for formatted output
   - Include descriptive text with values

4. **Code Organization**: Keep code clean and readable
   - Add blank lines between logical sections
   - Avoid overly complex nesting

### Error Handling

- Only use `try`/`except` for file operations
- Use specific exception types: `FileNotFoundError`, `ValueError`, `IndexError`
- Keep error handling simple and clear

### Prohibited Python Features

**DO NOT USE:**
- While loops
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions
- Lambda functions
- Decorators
- Classes and object-oriented programming
- Advanced function features (default arguments, *args, **kwargs)
- Context managers (except `with open()` for files)
- Regular expressions
- Threading or multiprocessing
- Any modules not explicitly listed in allowed concepts
- F-strings with format specifiers beyond basic `:.2f` style formatting
- Advanced slicing with step (`[::2]`)
- Unpacking beyond simple tuple unpacking in loops and returns
- Type hints or annotations

### Module Usage

**ONLY use these modules:**
- `math` (with allowed functions only)
- `numpy` (as `np`, with allowed functions only)
- `pandas` (as `pd`, with allowed functions only)
- `matplotlib.pyplot` (as `plt`, with allowed functions only)

**DO NOT import or suggest:**
- `os`, `sys`, `pathlib`
- `datetime`, `time`
- `random` (use `numpy.random` instead)
- `collections`
- `itertools`
- `functools`
- Any other standard library or third-party modules

---

## Code Generation Approach

When generating code:

1. **Use student-appropriate patterns**: Only use syntax and approaches shown in the course materials
2. **Keep it simple**: Prefer straightforward solutions over clever tricks
3. **Match the teaching style**: Use similar variable names, comments, and structure as the examples
4. **Provide context**: Include pharmaceutical or scientific context in examples
5. **Be explicit**: Avoid implicit behaviors or advanced Python features
6. **Educational focus**: Write code that reinforces the concepts students have learned
7. **Comment exhaustively**: Every generated code block must be heavily commented with beginner-friendly explanations
   - Assume the student is seeing this programming concept for the first time
   - Explain each step clearly and thoroughly
   - Use comments to teach, not just to describe
   - Connect code operations to real-world pharmaceutical/scientific meaning

---

## Examples of CORRECT Code Generation

### Good Example 1: Processing Patient Data
```python
# Create a list to store patient names
# Lists allow us to store multiple values in a single variable
patient_names = ["Alice Johnson", "Bob Smith", "Carol Davis"]

# Create a parallel list to store patient weights in kilograms
# The order matches patient_names (first weight goes with first name, etc.)
patient_weights = [68.0, 85.0, 52.0]

# Store the drug name we're calculating doses for
drug_name = "Amoxicillin"

# Define the dosing rate: 15 mg of drug per kg of patient body weight
# This is a standard weight-based dosing calculation in pharmacy
dose_per_kg = 15.0

# Loop through each patient to calculate their individual dose
# enumerate() gives us both the position (index) and the value (name)
for index, name in enumerate(patient_names):
    # Get the weight for this patient using the same index position
    weight = patient_weights[index]
    
    # Calculate the dose: multiply weight by dose rate
    # Example: 68 kg × 15 mg/kg = 1020 mg
    dose = dose_per_kg * weight
    
    # Display the result in a readable format
    # f-string allows us to insert variables into the text
    print(f"{name}: {weight} kg → {dose} mg of {drug_name}")
```

### Good Example 2: Reading and Filtering Data
```python
# Import the pandas library for working with tabular data
# We use the standard abbreviation 'pd'
import pandas as pd

# Import the numpy library for mathematical operations
# We use the standard abbreviation 'np'
import numpy as np

# Read compound data from a CSV file into a DataFrame
# A DataFrame is like a spreadsheet or table with rows and columns
df = pd.read_csv('compounds.csv')

# Filter the data to find drug-like compounds using Lipinski's Rule of 5
# This rule helps identify molecules that are likely to be good oral drugs
# We check three conditions using the & (and) operator:
# 1. Molecular weight should be 500 or less
# 2. LogP (lipophilicity) should be 5 or less
# 3. IC50 (potency) should be less than 20 µM (more potent)
drug_like = df[
    (df['molecular_weight'] <= 500) &
    (df['logp'] <= 5) &
    (df['ic50_um'] < 20)
]

# Calculate pIC50 from IC50 values
# pIC50 is a logarithmic transformation that makes values easier to compare
# Formula: pIC50 = -log10(IC50 in molar units)
# First divide by 1,000,000 to convert µM to M (molar)
# Then take -log10 of the result
drug_like['pic50'] = -np.log10(drug_like['ic50_um'] / 1_000_000)

# Display how many drug-like compounds we found
# len() gives us the number of rows in the filtered DataFrame
print(f"Found {len(drug_like)} drug-like compounds")

# Display the relevant columns for these compounds
# We select only the columns we're interested in: name, molecular_weight, logp, pic50
print(drug_like[['name', 'molecular_weight', 'logp', 'pic50']])
```

---

## Examples of INCORRECT Code Generation

### Bad Example 1: Using While Loop (NOT ALLOWED)
```python
# ❌ WRONG - Students have not learned while loops
count = 0
while count < len(patient_list):
    process_patient(patient_list[count])
    count += 1
```

**Correct approach:**
```python
# ✓ CORRECT - Use for loop (students have learned this)
# Loop through each patient in the patient list
for patient in patient_list:
    # Process this patient's information
    process_patient(patient)
```

### Bad Example 2: Using List Comprehension (NOT ALLOWED)
```python
# ❌ WRONG - Students have not learned list comprehensions
doses = [weight * dose_per_kg for weight in patient_weights]
```

**Correct approach:**
```python
# ✓ CORRECT - Use for loop with append (students have learned this)
# Create an empty list to store the calculated doses
doses = []

# Loop through each weight in the patient_weights list
for weight in patient_weights:
    # Calculate the dose for this patient weight
    # Multiply weight by the dose per kilogram
    dose = weight * dose_per_kg
    
    # Add this calculated dose to our doses list
    doses.append(dose)
```

### Bad Example 3: Using Lambda Functions (NOT ALLOWED)
```python
# ❌ WRONG - Students have not learned lambda functions
sorted_compounds = sorted(compounds, key=lambda x: x['ic50'])
```

**Correct approach:**
```python
# ✓ CORRECT - Use pandas sort_values (students have learned this)
# Sort the DataFrame by the 'ic50' column in ascending order
# This puts the most potent compounds (lowest IC50) at the top
df_sorted = df.sort_values('ic50')
```

### Bad Example 4: Using Advanced String Methods (NOT ALLOWED)
```python
# ❌ WRONG - Students have not learned join()
drug_list_string = ", ".join(drug_names)
```

**Correct approach:**
```python
# ✓ CORRECT - Use for loop for custom formatting (students have learned this)
# Create an empty string to build our result
result = ""

# Loop through each drug name with its position (index)
# enumerate() gives us both the index number and the drug name
for index, drug in enumerate(drug_names):
    # Check if this is the first drug (index 0)
    if index == 0:
        # For the first drug, just store the name without a comma
        result = drug
    else:
        # For all other drugs, add a comma and space before the name
        # We combine the existing result with the new drug name
        result = f"{result}, {drug}"
```

---

## Summary

Generate code that:
- ✓ Uses only the concepts explicitly taught to students
- ✓ Matches the style and patterns from course materials
- ✓ Includes **EXHAUSTIVE, beginner-friendly comments** explaining every step (on line before code, never inline)
- ✓ Comments explain WHAT, WHY, and HOW for every operation
- ✓ Comments teach programming concepts assuming the reader is a beginner
- ✓ Uses clear, descriptive variable names
- ✓ Focuses on pharmaceutical and scientific contexts
- ✓ Keeps solutions simple and educational
- ✗ Does NOT use advanced Python features
- ✗ Does NOT use while loops, comprehensions, or lambda functions
- ✗ Does NOT import modules beyond the allowed list
- ✗ Does NOT use shortcuts that students haven't learned

**CRITICAL: Every line or logical block of generated code MUST have a clear, educational comment. The student should be able to understand the entire program by reading the comments alone.**

**When in doubt, prefer the simpler, more explicit approach that students can easily understand based on what they've been taught.**
