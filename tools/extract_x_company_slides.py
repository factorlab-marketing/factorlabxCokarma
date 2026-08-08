import os
import re

input_file = r'c:\Users\Admin\Desktop\cokarma pitch deck\Sketch Brains pitch deck code.txt'
out_dir = r'c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides'

os.makedirs(out_dir, exist_ok=True)

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

slides = re.split(r'(?im)^slide\s+\d+\s*$', content)

slide_num = 1
for s in slides:
    s = s.strip()
    if s.startswith('<!DOCTYPE html>'):
        filepath = os.path.join(out_dir, f'slide_{slide_num}.html')
        with open(filepath, 'w', encoding='utf-8') as f_out:
            f_out.write(s)
        slide_num += 1

print(f"Created {slide_num - 1} slides in {out_dir}")
