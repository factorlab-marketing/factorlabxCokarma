
import os
import re

base_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_deck\slides"

for i in range(2, 30):
    filename = f"slide_{i}.html"
    filepath = os.path.join(base_dir, filename)
    
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Remove Sidebar HTML Block
    # Look for <div class="sidebar">...</div> immediately followed by <div class="main-content">
    content = re.sub(r'<div class="sidebar">.*?</div>\s*(?=<div class="main-content">)', '', content, flags=re.DOTALL)

    # 2. Update CSS
    content = content.replace('.slide-layout { display: flex;', '.slide-layout { display: block;')
    content = content.replace('.sidebar { width: 80px;', '.sidebar { display: none;')
    content = content.replace('.main-content { flex: 1;', '.main-content { width: 100%; height: 100%;')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes needed for {filename}")
