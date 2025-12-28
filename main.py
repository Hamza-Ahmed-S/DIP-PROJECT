"""
Main Runner Script for Bioinformatics Project
Executes all 4 requirements sequentially
"""

import sys

print("\n")
print("╔" + "═" * 78 + "╗")
print("║" + " " * 20 + "BIOINFORMATICS USING PYTHON" + " " * 31 + "║")
print("║" + " " * 25 + "Digital Image Processing Project" + " " * 21 + "║")
print("╚" + "═" * 78 + "╝")
print("\n")

# Menu
print("Select which requirement to run:")
print("  1. Requirement 1: ATP Hydrolysis Analysis")
print("  2. Requirement 2: DNA and Protein Sequence Analysis")
print("  3. Requirement 3: Advanced DNA/Protein Analysis")
print("  4. Requirement 4: N50 Calculation")
print("  5. Run ALL requirements")
print("  0. Exit")
print()

try:
    choice = input("Enter your choice (0-5): ").strip()
    print()
    
    if choice == "1":
        print("Running Requirement 1...\n")
        exec(open('requirement1.py').read())
    
    elif choice == "2":
        print("Running Requirement 2...\n")
        exec(open('requirement2.py').read())
    
    elif choice == "3":
        print("Running Requirement 3...\n")
        exec(open('requirement3.py').read())
    
    elif choice == "4":
        print("Running Requirement 4...\n")
        exec(open('requirement4.py').read())
    
    elif choice == "5":
        print("Running ALL requirements...\n")
        print("\n")
        exec(open('requirement1.py').read())
        print("\n" * 2)
        exec(open('requirement2.py').read())
        print("\n" * 2)
        exec(open('requirement3.py').read())
        print("\n" * 2)
        exec(open('requirement4.py').read())
        print("\n")
        print("╔" + "═" * 78 + "╗")
        print("║" + " " * 25 + "ALL REQUIREMENTS COMPLETED!" + " " * 26 + "║")
        print("╚" + "═" * 78 + "╝")
    
    elif choice == "0":
        print("Exiting...")
        sys.exit(0)
    
    else:
        print("Invalid choice! Please run again and select 0-5.")
        sys.exit(1)

except FileNotFoundError as e:
    print(f"Error: Could not find requirement file - {e}")
    print("Make sure all requirement files (requirement1.py, requirement2.py, etc.) are in the same directory.")
    sys.exit(1)

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
