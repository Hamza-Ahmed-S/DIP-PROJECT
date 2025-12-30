# Fix deprecation warning: replace use_container_width with width
import os

files_to_fix = [
    "pages/1_🧪_ATP_Hydrolysis.py",
    "pages/2_🧬_DNA_Analysis.py",
    "pages/4_📊_N50_Calculator.py",
    "pages/5_📈_Analytics_Dashboard.py"
]

for file_path in files_to_fix:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace use_container_width=True with width='stretch'
        updated_content = content.replace('use_container_width=True', "width='stretch'")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Fixed {file_path}")
    else:
        print(f"❌ Not found: {file_path}")

print("\n🎉 All deprecation warnings fixed!")
