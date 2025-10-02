"""
Reading Files in Python
========================

What is file reading?
---------------------
File reading allows programs to access data stored in external files. Instead
of typing data into the program every time, we can read it from files.

Why is file reading important in pharmacy?
------------------------------------------
Pharmacies work with data stored in files:
- Patient medication lists
- Drug inventory databases
- Prescription records
- Supplier price lists

Reading files lets us process large amounts of data efficiently.

The 'with' statement:
---------------------
The 'with' statement is the best practice for file operations because it:
- Automatically closes the file when done
- Handles errors properly
- Prevents data corruption

Syntax:
    with open('filename.txt', 'r') as file:
        # code to read the file

The 'r' means "read mode" (as opposed to 'w' for write or 'a' for append).

Practical Example: Reading pharmacy inventory from a file
"""

print("=" * 60)
print("Pharmacy File Processing System")
print("=" * 60)
print()

# Example 1: Reading entire file content at once
print("Example 1: Reading complete file")
print("-" * 60)

filename = "drug_inventory.txt"

try:
    # Using 'with' statement to open file safely
    with open(filename, 'r', encoding='utf-8') as file:
        # Read entire file content
        content = file.read()
        print("File contents:")
        print(content)
    
    print("✓ File closed automatically after 'with' block")
    
except FileNotFoundError:
    print(f"⚠ Error: File '{filename}' not found!")
    print("Please make sure the file exists in the same directory.")

print()

# Example 2: Reading file line by line
print("Example 2: Processing file line by line")
print("-" * 60)

try:
    with open(filename, 'r', encoding='utf-8') as file:
        line_number = 1
        
        # Loop through each line in the file
        for line in file:
            # Remove whitespace and newline characters
            line = line.strip()
            print(f"Line {line_number}: {line}")
            line_number += 1
    
except FileNotFoundError:
    print(f"⚠ Error: File '{filename}' not found!")

print()

# Example 3: Reading and parsing structured data
print("Example 3: Parsing drug inventory data")
print("-" * 60)

try:
    with open(filename, 'r', encoding='utf-8') as file:
        print("Drug Inventory Report")
        print()
        
        for line in file:
            # Remove whitespace
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Split line by comma to get individual fields
            parts = line.split(',')
            
            # Extract each field
            drug_name = parts[0]
            dosage = parts[1]
            price = parts[2]
            expiry_date = parts[3]
            
            # Display formatted information
            print(f"Drug: {drug_name}")
            print(f"  Dosage: {dosage}")
            print(f"  Price: ${price}")
            print(f"  Expiry: {expiry_date}")
            print()

except FileNotFoundError:
    print(f"⚠ Error: File '{filename}' not found!")

print()

# Example 4: Calculating statistics from file data
print("Example 4: Calculating inventory statistics")
print("-" * 60)

try:
    with open(filename, 'r', encoding='utf-8') as file:
        total_drugs = 0
        total_value = 0.0
        drug_list = []
        
        for line in file:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Parse the line
            parts = line.split(',')
            drug_name = parts[0]
            price = float(parts[2])  # Convert string to float
            
            # Update statistics
            total_drugs += 1
            total_value += price
            drug_list.append(drug_name)
        
        # Display statistics
        print(f"Total medications in inventory: {total_drugs}")
        print(f"Total inventory value: ${total_value:.2f}")
        print(f"Average price per medication: ${total_value / total_drugs:.2f}")
        print()
        print("Medication list:")
        for drug in drug_list:
            print(f"  - {drug}")

except FileNotFoundError:
    print(f"⚠ Error: File '{filename}' not found!")
except ValueError:
    print("⚠ Error: Invalid data format in file!")

print()

# Example 5: Filtering data based on conditions
print("Example 5: Finding medications expiring soon")
print("-" * 60)

try:
    with open(filename, 'r', encoding='utf-8') as file:
        current_year = 2025
        expiring_soon = []
        
        for line in file:
            line = line.strip()
            
            if not line:
                continue
            
            parts = line.split(',')
            drug_name = parts[0]
            expiry_date = parts[3]
            
            # Extract year from expiry date (format: YYYY-MM-DD)
            expiry_year = int(expiry_date.split('-')[0])
            
            # Check if expiring in current year or already expired
            if expiry_year <= current_year:
                expiring_soon.append((drug_name, expiry_date))
        
        # Display results
        print(f"Medications expiring in {current_year} or earlier:")
        print()
        
        if expiring_soon:
            for drug, expiry in expiring_soon:
                print(f"⚠ {drug} - Expires: {expiry}")
        else:
            print("✓ No medications expiring soon")

except FileNotFoundError:
    print(f"⚠ Error: File '{filename}' not found!")
except (ValueError, IndexError):
    print("⚠ Error: Invalid date format in file!")

print()

print("=" * 60)
print("Key Takeaway:")
print("Use 'with open()' to read files safely. The file is automatically")
print("closed when done. Always use try/except to handle file errors.")
print("Process files line by line for efficiency with large files.")
print("=" * 60)
