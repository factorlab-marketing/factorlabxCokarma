import os
import re

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

connector_str_4 = '''<!-- Connector -->
<div class="flex flex-col items-center px-2">
<div class="h-1 w-8 rounded-full arrow-line"></div>
<div class="mt-2">
<i class="fa-solid fa-arrow-right muted"></i>
</div>
</div>'''

connector_str_8 = '''<!-- Connector -->
<div class="flex flex-col items-center px-2">
<div class="h-1 w-12 rounded-full arrow-line"></div>
<div class="mt-2">
<i class="fa-solid fa-arrow-right muted"></i>
</div>
</div>'''

def fix_slide_4(html):
    html = html.replace('<div class="flex items-center justify-between">\n<!-- Step 1 -->\n<div class="w-56">', '<div class="grid grid-cols-2 gap-3">\n<!-- Step 1 -->\n<div>')
    html = html.replace('<div class="w-56">', '<div>')
    html = html.replace(connector_str_4, "")
    return html

def fix_slide_8(html):
    html = html.replace('<div class="flex items-center justify-between">\n<!-- Node 1 -->\n<div class="w-56">', '<div class="grid grid-cols-2 gap-3">\n<!-- Node 1 -->\n<div>')
    html = html.replace('<div class="w-56">', '<div>')
    html = html.replace(connector_str_8, "")
    # also scale down vertical
    html = html.replace('p-5 fine-border', 'p-3 fine-border')
    return html

def fix_slide_5(html):
    html = html.replace('p-5 fine-border', 'p-3 fine-border')
    html = html.replace('mt-7 rounded-2xl', 'mt-3 rounded-2xl')
    html = html.replace('p-5 flex-1', 'p-3 flex-1')
    html = html.replace('mt-4 flex items-center', 'mt-2 flex items-center')
    html = html.replace('text-2xl font-extrabold', 'text-xl font-extrabold')
    # shrink badges slightly
    html = html.replace('w-12 h-12', 'w-10 h-10')
    html = html.replace('w-9 h-9', 'w-8 h-8')
    return html

def fix_slide_7(html):
    # cost logic override
    html = html.replace('w-72 rounded-2xl', 'flex-1 rounded-2xl')
    # scale pad
    html = html.replace('p-4 fine-border', 'p-3 fine-border')
    html = html.replace('p-5 fine-border', 'p-3 fine-border')
    html = html.replace('text-2xl font-extrabold', 'text-lg font-extrabold')
    return html

def fix_slide_9(html):
    html = html.replace('p-4 fine-border', 'p-3 fine-border')
    html = html.replace('p-5 flex-1', 'p-3 flex-1')
    html = html.replace('text-2xl font-extrabold', 'text-lg font-extrabold')
    html = html.replace('mt-4 flex items-center', 'mt-2 flex items-center')
    html = html.replace('w-12 h-12', 'w-10 h-10')
    return html

for i in [4, 5, 7, 8, 9]:
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if i == 4:
        content = fix_slide_4(content)
    if i == 8:
        content = fix_slide_8(content)
    if i == 5:
        content = fix_slide_5(content)
    if i == 7:
        content = fix_slide_7(content)
    if i == 9:
        content = fix_slide_9(content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Targeted fixes applied.")
