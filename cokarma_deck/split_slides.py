import re
import os

# Define the input file path
input_file_path = "Factorlab x CoKarma survey pitch de.txt"
output_dir = "slides"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def split_slides(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split by the "slide - \d+" marker
    # The regex looks for lines that start with "slide - " followed by numbers
    # We use re.split capturing the delimiter to keep track of slide numbers if needed, 
    # but re.finditer might be better to get position.
    
    # Actually, let's just use a pattern to identify the start of chunks
    pattern = re.compile(r'^slide - \s*(\d+)', re.MULTILINE | re.IGNORECASE)
    
    matches = list(pattern.finditer(content))
    
    if not matches:
        print("No slides found.")
        return

    for i in range(len(matches)):
        start_index = matches[i].end()
        # End index is the start of the next match, or end of file
        end_index = matches[i+1].start() if i + 1 < len(matches) else len(content)
        
        slide_num = matches[i].group(1)
        slide_content = content[start_index:end_index].strip()
        
        # Determine output filename
        output_filename = os.path.join(output_dir, f"slide_{slide_num}.html")
        
        # Inject the message listener script before </body>
        script_content = """
    <script>
        window.addEventListener('message', function(event) {
            if (event.data.type === 'theme-update') {
                const isDark = event.data.isDark;
                const css = event.data.css;
                const styleId = 'dark-theme-style';
                let style = document.getElementById(styleId);
                
                if (isDark) {
                    if (!style) {
                        style = document.createElement('style');
                        style.id = styleId;
                        style.textContent = css;
                        document.head.appendChild(style);
                    }
                } else {
                    if (style) {
                        style.remove();
                    }
                }
            }
        });
    </script>
    </body>
"""
        
        # Replace </body> with our script + </body>
        # Using simple string replace might be risky if case varies, but typically it is </body>
        if "</body>" in slide_content:
            slide_content = slide_content.replace("</body>", script_content.replace("    </body>", "")) + "</body>"
        else:
            # If no body tag, append to end
            slide_content += script_content
        
        # Write to file
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(slide_content)
        
        print(f"Created {output_filename}")

if __name__ == "__main__":
    split_slides(input_file_path)
