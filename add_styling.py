# Quick script to add styling to remaining pages
import os

# Pages to update
pages_to_update = [
    "pages/3_🔬_Advanced_Analysis.py",
    "pages/4_📊_N50_Calculator.py",
    "pages/5_📈_Analytics_Dashboard.py",
    "pages/6_📝_Feedback_Survey.py"
]

styling_import = """
# Apply shared styling
from utils.shared_styling import apply_common_styling
apply_common_styling()
"""

for page_path in pages_to_update:
    if os.path.exists(page_path):
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only add if not already there
        if 'apply_common_styling' not in content:
            # Find st.set_page_config line
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'st.set_page_config' in line:
                    # Insert before this line
                    lines.insert(i, styling_import)
                    break
            
            # Write back
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            
            print(f"✅ Added styling to {page_path}")
        else:
            print(f"⏭️  Styling already in {page_path}")
    else:
        print(f"❌ File not found: {page_path}")

print("\n🎉 Done!")
