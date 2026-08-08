import os
from bs4 import BeautifulSoup

slides_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"
script_tag_html = '<script src="../../js/capture_helper.js"></script>'

def inject_capture_helper():
    count = 0
    for filename in os.listdir(slides_dir):
        if not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(slides_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if already injected
        if "capture_helper.js" in content:
            continue
            
        # Inject right before </body> or at the end of the file
        if "</body>" in content:
            new_content = content.replace("</body>", f"{script_tag_html}\n</body>")
        else:
            new_content = content + f"\n{script_tag_html}"
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
            
    print(f"Successfully injected capture_helper.js into {count} slides.")

if __name__ == "__main__":
    inject_capture_helper()
