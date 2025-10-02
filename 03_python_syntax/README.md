# Python Syntax for Molecular Modeling in Drug Design

This directory contains Python teaching materials for pharmacy students learning programming basics through pharmaceutical examples.

## Setup

### Virtual Environment

A virtual environment has been created in the parent directory (`../PMMiDD_venv`) with all required packages.

### Activating the Virtual Environment

**On macOS/Linux:**
```bash
source "../PMMiDD_venv/bin/activate"
```

**On Windows:**
```cmd
..\PMMiDD_venv\Scripts\activate
```

### Installing Dependencies

If you need to reinstall or update packages:
```bash
pip install -r requirements.txt
```

### Required Packages

- **numpy** (2.0.2): Numerical computing and array operations
- **pandas** (2.3.3): Data manipulation and analysis
- **matplotlib** (3.9.4): Data visualization and plotting

## Python Files Overview

### Basic Python Syntax (00-09)

1. **00_variables_and_data_types.py** - Variables, integers, floats, strings
2. **01_lists.py** - List operations, indexing, slicing, methods
3. **02_dictionaries.py** - Dictionary operations, key-value pairs
4. **03_string_operations.py** - String manipulation, split, replace, count
5. **04_conditionals.py** - if/elif/else statements, decision making
6. **05_for_loops.py** - Loop operations, enumerate, iterations
7. **06_functions.py** - Function definition, parameters, return values
8. **07_reading_files.py** - File operations, reading CSV data
9. **08_math_module.py** - Math functions for pharmaceutical calculations
10. **09_copilot_exercise.py** - GitHub Copilot pseudo-code exercise

### Scientific Computing (10-12)

11. **10_numpy_arrays.py** - NumPy arrays for molecular data analysis
12. **11_pandas_dataframes.py** - Pandas DataFrames for structured data
13. **12_matplotlib_plots.py** - Matplotlib for data visualization

## Data Files

- **drug_inventory.txt** - Sample drug inventory data
- **compounds_data.csv** - Molecular property database
- **drug_like_compounds.csv** - Filtered drug-like compounds (generated)

## Running the Examples

After activating the virtual environment:

```bash
# Basic examples (no dependencies)
python 00_variables_and_data_types.py
python 01_lists.py
# ... etc

# Scientific computing examples (requires numpy, pandas, matplotlib)
python 10_numpy_arrays.py
python 11_pandas_dataframes.py
python 12_matplotlib_plots.py
```

## Learning Path

Follow the files in numerical order:
1. Start with basic Python syntax (00-09)
2. Move to scientific computing libraries (10-12)
3. Practice with the Copilot exercise (09)

## Notes

- All examples use practical pharmaceutical scenarios
- Print statements are optimized for clarity
- Each file is self-contained and runnable
- Comments explain concepts and provide context

## Deactivating the Virtual Environment

When finished:
```bash
deactivate
```

---

*Course: Molecular Modeling in Drug Design*  
*Target Audience: Pharmacy students (beginners in programming)*
