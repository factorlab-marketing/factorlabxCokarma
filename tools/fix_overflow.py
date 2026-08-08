import os
import re

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

replacements = {
    r'\btext-6xl\b': 'text-5xl',
    r'\btext-5xl\b': 'text-4xl',
    r'\btext-4xl\b': 'text-3xl',
    r'\btext-3xl\b': 'text-2xl',
    
    r'\bpy-14\b': 'py-8',
    r'\bpx-16\b': 'px-10',
    r'\bpr-10\b': 'pr-6',
    
    r'\bp-10\b': 'p-6',
    r'\bp-8\b': 'p-5',
    r'\bp-7\b': 'p-5',
    r'\bp-6\b': 'p-4',
    
    r'\bmb-10\b': 'mb-5',
    r'\bmb-8\b': 'mb-4',
    r'\bmb-6\b': 'mb-3',
    r'\bmb-5\b': 'mb-2',
    
    r'\bmt-10\b': 'mt-5',
    r'\bmt-8\b': 'mt-4',
    r'\bmt-6\b': 'mt-3',
    r'\bmt-5\b': 'mt-2',
    
    r'\bspace-y-6\b': 'space-y-3',
    r'\bspace-y-4\b': 'space-y-2',
    r'\bspace-x-4\b': 'space-x-3',
    r'\bspace-x-3\b': 'space-x-2',
    
    r'\bw-11\b': 'w-9',
    r'\bh-11\b': 'h-9',
    r'\bw-10\b': 'w-8',
    r'\bh-10\b': 'h-8'
}

for i in range(1, 10):
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for k, v in replacements.items():
        content = re.sub(k, v, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Scaling adjustments applied.")
