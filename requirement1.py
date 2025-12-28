"""
Requirement 1: ATP Hydrolysis Thermodynamics Analysis

Calculate ΔG (Gibbs free energy) values for ATP hydrolysis in three tissues,
determine the most exothermic reaction, and convert energy values from 
kilojoules (KJ) to kilocalories (kcal).
"""

print("=" * 80)
print("REQUIREMENT 1: ATP HYDROLYSIS ANALYSIS")
print("=" * 80)
print()

# ATP Hydrolysis data for three tissues (example data)
# ΔG = ΔG° + RT ln([ADP][Pi]/[ATP])
# Using typical cellular conditions for different tissues

tissues_data = {
    "Liver": {
        "ATP": 3.5,      # mM
        "ADP": 1.3,      # mM
        "Pi": 5.0,       # mM
        "delta_G0": -30.5  # kJ/mol (standard free energy)
    },
    "Muscle": {
        "ATP": 8.0,      # mM
        "ADP": 0.9,      # mM
        "Pi": 8.0,       # mM
        "delta_G0": -30.5  # kJ/mol
    },
    "Brain": {
        "ATP": 2.6,      # mM
        "ADP": 0.7,      # mM
        "Pi": 2.7,       # mM
        "delta_G0": -30.5  # kJ/mol
    }
}

# Constants
R = 8.314e-3  # Gas constant in kJ/(mol·K)
T = 310       # Temperature in Kelvin (37°C, body temperature)
KJ_TO_KCAL = 0.239006  # Conversion factor: 1 kJ = 0.239006 kcal

print("ATP Hydrolysis: ATP + H2O → ADP + Pi + H+\n")
print("Calculating ΔG for each tissue:\n")

# Calculate ΔG for each tissue
delta_g_values = {}

for tissue, data in tissues_data.items():
    # Calculate Q (reaction quotient)
    Q = (data["ADP"] * data["Pi"]) / data["ATP"]
    
    # Calculate ΔG using the equation: ΔG = ΔG° + RT ln(Q)
    import math
    delta_G = data["delta_G0"] + (R * T * math.log(Q))
    
    delta_g_values[tissue] = delta_G
    
    print(f"{tissue}:")
    print(f"  [ATP] = {data['ATP']} mM")
    print(f"  [ADP] = {data['ADP']} mM")
    print(f"  [Pi]  = {data['Pi']} mM")
    print(f"  Q = ([ADP][Pi])/[ATP] = {Q:.4f}")
    print(f"  ΔG° = {data['delta_G0']} kJ/mol")
    print(f"  ΔG = {delta_G:.2f} kJ/mol")
    print()

# Find the most exothermic tissue (most negative ΔG)
most_exothermic_tissue = min(delta_g_values, key=delta_g_values.get)
most_exothermic_value = delta_g_values[most_exothermic_tissue]

print("-" * 80)
print(f"\nMost Exothermic Tissue: {most_exothermic_tissue}")
print(f"ΔG = {most_exothermic_value:.2f} kJ/mol")
print(f"\nNote: More negative ΔG means more energy is released (more exothermic)")
print()

# Convert all values from kJ to kcal
print("-" * 80)
print("\nConversion from kJ to kcal (1 kJ = 0.239006 kcal):\n")

for tissue, delta_G_kj in delta_g_values.items():
    delta_G_kcal = delta_G_kj * KJ_TO_KCAL
    print(f"{tissue}:")
    print(f"  ΔG = {delta_G_kj:.2f} kJ/mol = {delta_G_kcal:.2f} kcal/mol")
    print()

print("=" * 80)
print("REQUIREMENT 1 COMPLETED")
print("=" * 80)
