import os
import re
from bs4 import BeautifulSoup

def compile_booklet():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pages_dir = os.path.join(base_dir, "pages")
    
    total_pages = 24
    
    # Left pages definition
    left_pages = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    
    compiled_pages_html = ""
    print_pages_html = ""
    
    print("Reading and parsing page HTML files...")
    
    for i in range(1, total_pages + 1):
        page_file_name = f"page_{i}.html"
        page_path = os.path.join(pages_dir, page_file_name)
        
        if not os.path.exists(page_path):
            print(f"Error: {page_file_name} not found!")
            return
            
        with open(page_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        soup = BeautifulSoup(html_content, "html.parser")
        page_content_div = soup.find(class_="page-content")
        
        if not page_content_div:
            print(f"Error: class='page-content' not found in {page_file_name}")
            return
            
        # Build DOM block for index_compiled.html
        compiled_pages_html += f'                <div class="page" data-page="{i}">\n'
        compiled_pages_html += f'                    <div class="page-content">\n'
        compiled_pages_html += f'                        {page_content_div.decode_contents().strip()}\n'
        compiled_pages_html += f'                    </div>\n'
        compiled_pages_html += f'                </div>\n\n'
        
        # Build DOM block for print_compiled.html
        print_pages_html += f'        <div class="page" data-page="{i}">\n'
        print_pages_html += f'            <div class="page-content">\n'
        print_pages_html += f'                {page_content_div.decode_contents().strip()}\n'
        print_pages_html += f'            </div>\n'
        print_pages_html += f'        </div>\n\n'

    # Compile index.html
    index_path = os.path.join(base_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()
        
    # Replace container content
    index_soup = BeautifulSoup(index_html, "html.parser")
    book_container = index_soup.find(class_="book-container")
    if book_container:
        book_container.clear()
        book_container.append(BeautifulSoup(compiled_pages_html, "html.parser"))
    # Override print button behavior for standalone mode
    override_script = index_soup.new_tag("script")
    override_script.string = """
        document.addEventListener('DOMContentLoaded', () => {
            const printBtn = document.getElementById('print-btn');
            if (printBtn) {
                const newPrintBtn = printBtn.cloneNode(true);
                printBtn.parentNode.replaceChild(newPrintBtn, printBtn);
                newPrintBtn.addEventListener('click', () => {
                    window.open('print_compiled.html', '_blank');
                });
            }
        });
    """
    index_soup.body.append(override_script)
    
    compiled_index_path = os.path.join(base_dir, "index_compiled.html")
    with open(compiled_index_path, "w", encoding="utf-8") as f:
        f.write(str(index_soup))
    print("Successfully generated index_compiled.html")

    # Compile print.html
    print_path = os.path.join(base_dir, "print.html")
    with open(print_path, "r", encoding="utf-8") as f:
        print_html = f.read()
        
    # Remove dynamic fetch loader script from print_compiled.html since pages are already inline
    # Replace print container content
    print_soup = BeautifulSoup(print_html, "html.parser")
    print_container = print_soup.find(id="print-container")
    if print_container:
        print_container.clear()
        print_container.append(BeautifulSoup(print_pages_html, "html.parser"))
        
    # Remove script loading logic and just trigger window.print
    status_overlay = print_soup.find(id="status-overlay")
    if status_overlay:
        status_overlay.decompose()
        
    script_tags = print_soup.find_all("script")
    for script in script_tags:
        if "loadAndPrint" in script.text:
            script.string = """
                window.addEventListener('load', async () => {
                    await document.fonts.ready;
                    setTimeout(() => {
                        window.print();
                    }, 500);
                });
            """
            
    compiled_print_path = os.path.join(base_dir, "print_compiled.html")
    with open(compiled_print_path, "w", encoding="utf-8") as f:
        f.write(str(print_soup))
    print("Successfully generated print_compiled.html")
    print("Done! You can now double-click index_compiled.html to run the booklet locally.")

if __name__ == "__main__":
    compile_booklet()
