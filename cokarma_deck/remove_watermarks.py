import os
from bs4 import BeautifulSoup
import glob

def remove_watermarks():
    files = glob.glob('slides/slide_*.html')
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        modified = False

        # Strategy 1: Find elements with text "FactorLab" that are absolutely positioned or in footer
        # We need to be careful not to delete the Title "Introduction to FactorLab" etc.
        # Watermarks usually have class "absolute" and are small.
        
        # Search for tags containing exact text "FactorLab" or small variations
        for element in soup.find_all(string=lambda text: text and "FactorLab" in text):
            parent = element.parent
            
            # Check if it's likely a watermark
            # Indicators: absolute position, bottom/right alignment, small text, opacity
            classes = parent.get('class', [])
            
            # Check if it's the main title (h1) - SKIP
            if parent.name == 'h1' or parent.name == 'h2':
                continue
            if 'text-5xl' in classes or 'text-4xl' in classes: # Likely title
                continue
                
            # If it's a small tag inside a div/footer
            container = parent
            while container and container.name not in ['body', 'html']:
                c_classes = container.get('class', [])
                if 'absolute' in c_classes and ('bottom-4' in c_classes or 'bottom-6' in c_classes or 'right-6' in c_classes or 'right-8' in c_classes or 'top-10' in c_classes):
                    # This looks like a watermark container
                    container.decompose()
                    modified = True
                    break
                
                # Also check for footer tags that act as watermarks
                if container.name == 'footer' and ('absolute' in c_classes or 'text-right' in c_classes):
                     # Check if it contains ONLY the watermark stuff
                     if "FactorLab" in container.get_text():
                         container.decompose()
                         modified = True
                         break
                
                container = container.parent

        if modified:
            print(f"Removing watermark from {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

if __name__ == "__main__":
    remove_watermarks()
