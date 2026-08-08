
import os

slides_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_deck\slides"

# Script tag to inject
script_tag = '<script src="../../js/capture_helper.js"></script>'

count = 0
for filename in os.listdir(slides_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(slides_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check if already present to avoid duplicates
        if "capture_helper.js" in content:
            print(f"Skipping {filename} - already has capture script")
            continue
            
        # Inject before closing body tag
        if "</body>" in content:
            new_content = content.replace("</body>", f"    {script_tag}\n</body>")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
                
            print(f"Injected capture script into {filename}")
            count += 1
        else:
            print(f"Warning: No </body> tag found in {filename}")

print(f"Total slides updated: {count}")
