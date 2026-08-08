
import os

decks = [
    r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_deck\slides",
    r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_villa_marie_deck\slides"
]

script_tag = '<script src="../../js/capture_helper.js"></script>'

for slides_dir in decks:
    print(f"Processing directory: {slides_dir}")
    if not os.path.exists(slides_dir):
        print(f"Directory not found: {slides_dir}")
        continue
        
    count = 0
    for filename in os.listdir(slides_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(slides_dir, filename)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            if "capture_helper.js" in content:
                # print(f"Skipping {filename} - already has capture script")
                continue
                
            if "</body>" in content:
                new_content = content.replace("</body>", f"    {script_tag}\n</body>")
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                    
                print(f"Injected capture script into {filename}")
                count += 1
            else:
                print(f"Warning: No </body> tag found in {filename}")

    print(f"Total slides updated in this directory: {count}\n")
