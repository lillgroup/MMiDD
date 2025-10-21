"""
Data Visualization with Matplotlib
===================================

What is Matplotlib?
-------------------
Matplotlib is the foundational plotting library in Python for creating static,
animated, and interactive visualizations. It allows scientists to create
publication-quality graphs and figures.

Why is visualization important in drug design?
----------------------------------------------
In pharmaceutical research, we need to visualize:
- Dose-response curves (IC50 determination)
- Time-course data (pharmacokinetics)
- Structure-activity relationships (SAR)
- Molecular property distributions
- Experimental results for presentations and publications

"A picture is worth a thousand words" - visualizations help us:
- Identify trends and patterns
- Communicate results effectively
- Detect outliers and anomalies
- Make data-driven decisions

Standard convention: import matplotlib.pyplot as plt

Practical Example: Visualizing pharmaceutical data
"""

import matplotlib.pyplot as plt
import numpy as np

print("Matplotlib for Scientific Data Visualization\n")

# Example 1: Simple line plot - Drug concentration over time
print("Ex1: Creating a line plot (pharmacokinetics)\n")

# Time points (hours) and plasma concentration (µg/mL)
time_hours = np.array([0, 0.5, 1, 2, 4, 6, 8, 12, 24])
concentration = np.array([0, 8.5, 12.3, 15.2, 13.8, 11.5, 9.2, 6.4, 2.1])

plt.figure(figsize=(8, 5))
plt.plot(time_hours, concentration, marker='o', linewidth=2, color='blue')
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Plasma Concentration (µg/mL)', fontsize=12)
plt.title('Pharmacokinetic Profile of Drug X', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.savefig('pharmacokinetics_plot.png', dpi=300, bbox_inches='tight')
print("✓ Saved: pharmacokinetics_plot.png")
plt.close()

# Example 2: Scatter plot - Molecular weight vs LogP
print("Ex2: Creating a scatter plot (molecular properties)\n")

# Molecular properties for 15 compounds
mw = np.array([180, 206, 250, 310, 195, 280, 340, 225, 295, 265, 315, 240, 275, 305, 260])
logp = np.array([1.2, 3.9, 2.5, 3.8, 1.9, 3.2, 4.1, 2.8, 3.5, 3.0, 3.9, 2.3, 3.3, 3.7, 2.9])

plt.figure(figsize=(8, 6))
plt.scatter(mw, logp, s=100, c='red', alpha=0.6, edgecolors='black')
plt.xlabel('Molecular Weight (g/mol)', fontsize=12)
plt.ylabel('LogP', fontsize=12)
plt.title('Molecular Weight vs Lipophilicity', fontsize=14, fontweight='bold')
plt.axhline(y=5, color='orange', linestyle='--', label='LogP limit (Lipinski)')
plt.axvline(x=500, color='green', linestyle='--', label='MW limit (Lipinski)')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.savefig('mw_vs_logp_scatter.png', dpi=300, bbox_inches='tight')
print("✓ Saved: mw_vs_logp_scatter.png")
plt.close()

# Example 3: Dose-response curve (sigmoidal)
print("Ex3: Creating a dose-response curve\n")

# Generate dose-response data
doses = np.logspace(-9, -4, 50)  # 1 nM to 10 µM
# Sigmoidal curve: Response = 100 / (1 + (IC50/dose)^Hill_slope)
ic50 = 5e-7  # 500 nM
hill_slope = 1.0
response = 100 / (1 + (ic50 / doses) ** hill_slope)

plt.figure(figsize=(8, 5))
plt.semilogx(doses * 1e6, response, linewidth=2.5, color='purple')  # Convert to µM
plt.xlabel('Concentration (µM)', fontsize=12)
plt.ylabel('% Inhibition', fontsize=12)
plt.title('Dose-Response Curve (IC50 = 0.5 µM)', fontsize=14, fontweight='bold')
plt.axhline(y=50, color='gray', linestyle='--', alpha=0.5, label='50% inhibition')
plt.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5, label='IC50 = 0.5 µM')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(0, 105)
plt.savefig('dose_response_curve.png', dpi=300, bbox_inches='tight')
print("✓ Saved: dose_response_curve.png")
plt.close()

# Example 4: Bar plot - IC50 comparison across compounds
print("Ex4: Creating a bar plot (compound comparison)\n")

compounds = ['CPD-A', 'CPD-B', 'CPD-C', 'CPD-D', 'CPD-E', 'CPD-F']
ic50_values = np.array([3.2, 5.7, 8.9, 12.3, 2.1, 15.4])
colors = ['green' if x < 5 else 'orange' if x < 10 else 'red' for x in ic50_values]

plt.figure(figsize=(9, 6))
bars = plt.bar(compounds, ic50_values, color=colors, alpha=0.7, edgecolor='black')
plt.xlabel('Compound ID', fontsize=12)
plt.ylabel('IC50 (µM)', fontsize=12)
plt.title('Compound Potency Comparison', fontsize=14, fontweight='bold')
plt.axhline(y=10, color='red', linestyle='--', alpha=0.5, label='Target IC50 < 10 µM')
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar, value in zip(bars, ic50_values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             f'{value:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.savefig('ic50_comparison_bar.png', dpi=300, bbox_inches='tight')
print("✓ Saved: ic50_comparison_bar.png")
plt.close()

# Example 5: Multiple lines on one plot - Comparing drug candidates
print("Ex5: Multiple lines on one plot (compound comparison)\n")

time = np.linspace(0, 24, 25)
# Pharmacokinetic profiles for three compounds
compound_a = 10 * np.exp(-0.15 * time)
compound_b = 12 * np.exp(-0.10 * time)
compound_c = 8 * np.exp(-0.20 * time)

plt.figure(figsize=(9, 6))
plt.plot(time, compound_a, marker='o', label='Compound A (fast clearance)', linewidth=2)
plt.plot(time, compound_b, marker='s', label='Compound B (slow clearance)', linewidth=2)
plt.plot(time, compound_c, marker='^', label='Compound C (very fast clearance)', linewidth=2)
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Plasma Concentration (µg/mL)', fontsize=12)
plt.title('Pharmacokinetic Comparison of Drug Candidates', fontsize=14, fontweight='bold')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.savefig('pk_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: pk_comparison.png")
plt.close()

# Example 6: Subplots - Multiple related graphs
print("Ex6: Creating subplots (multiple related visualizations)\n")

# Generate data
compounds_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ic50_data = np.array([5.2, 3.4, 8.9, 2.1, 12.3, 4.5, 6.7, 9.8])
mw_data = np.array([250, 310, 280, 340, 195, 265, 290, 305])
logp_data = np.array([2.5, 3.8, 3.2, 4.1, 1.9, 3.0, 3.5, 3.7])

# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Compound Screening Results Dashboard', fontsize=16, fontweight='bold')

# Subplot 1: IC50 values
axes[0, 0].bar(compounds_list, ic50_data, color='steelblue', alpha=0.7)
axes[0, 0].set_ylabel('IC50 (µM)', fontsize=10)
axes[0, 0].set_title('Potency (IC50)', fontsize=12)
axes[0, 0].grid(axis='y', alpha=0.3)

# Subplot 2: Molecular weights
axes[0, 1].bar(compounds_list, mw_data, color='coral', alpha=0.7)
axes[0, 1].set_ylabel('Molecular Weight (g/mol)', fontsize=10)
axes[0, 1].set_title('Molecular Weight', fontsize=12)
axes[0, 1].axhline(y=500, color='red', linestyle='--', alpha=0.5)
axes[0, 1].grid(axis='y', alpha=0.3)

# Subplot 3: LogP distribution
axes[1, 0].hist(logp_data, bins=6, color='green', alpha=0.7, edgecolor='black')
axes[1, 0].set_xlabel('LogP', fontsize=10)
axes[1, 0].set_ylabel('Frequency', fontsize=10)
axes[1, 0].set_title('LogP Distribution', fontsize=12)
axes[1, 0].grid(axis='y', alpha=0.3)

# Subplot 4: MW vs LogP scatter
axes[1, 1].scatter(mw_data, logp_data, s=100, c=ic50_data, cmap='RdYlGn_r', 
                   alpha=0.7, edgecolors='black')
axes[1, 1].set_xlabel('Molecular Weight (g/mol)', fontsize=10)
axes[1, 1].set_ylabel('LogP', fontsize=10)
axes[1, 1].set_title('MW vs LogP (colored by IC50)', fontsize=12)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('compound_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Saved: compound_dashboard.png")
plt.close()

# Example 7: Histogram - Distribution analysis
print("Ex7: Creating a histogram (distribution analysis)\n")

# Generate IC50 data for 50 compounds
np.random.seed(42)
ic50_population = np.random.lognormal(mean=1.0, sigma=0.8, size=50)

plt.figure(figsize=(9, 6))
plt.hist(ic50_population, bins=15, color='teal', alpha=0.7, edgecolor='black')
plt.xlabel('IC50 (µM)', fontsize=12)
plt.ylabel('Number of Compounds', fontsize=12)
plt.title('IC50 Distribution in Compound Library (n=50)', fontsize=14, fontweight='bold')
plt.axvline(x=np.median(ic50_population), color='red', linestyle='--', 
            linewidth=2, label=f'Median = {np.median(ic50_population):.2f} µM')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('ic50_histogram.png', dpi=300, bbox_inches='tight')
print("✓ Saved: ic50_histogram.png")
plt.close()

print("\n" + "="*60)
print("Summary of saved plots:")
print("  1. pharmacokinetics_plot.png - Line plot")
print("  2. mw_vs_logp_scatter.png - Scatter plot")
print("  3. dose_response_curve.png - Sigmoidal curve")
print("  4. ic50_comparison_bar.png - Bar plot")
print("  5. pk_comparison.png - Multiple lines")
print("  6. compound_dashboard.png - Subplots (2x2)")
print("  7. ic50_histogram.png - Histogram")
print("="*60)

print("\n✓ Matplotlib: essential for creating scientific visualizations and figures.")
print("\nNote: Use plt.show() instead of plt.close() to display plots interactively.")
print("      plt.savefig() saves plots as image files (PNG, PDF, SVG, etc.)")
