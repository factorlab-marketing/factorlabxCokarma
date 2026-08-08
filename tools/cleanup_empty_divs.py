import os
from bs4 import BeautifulSoup
import re

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

for i in range(1, 10):
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    for div in soup.find_all('div', class_=re.compile(r'overflow-hidden')):
        if not div.find(True) and not div.text.strip():
            div.decompose()
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Cleaned up empty containers.")
