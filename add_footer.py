
import os

footer_html = """
    <div class="footer-strip">
        <div class="footer-text">Sketch Brains | 2026 Tech Career Blueprint</div>
        <div class="footer-logo"><i class="fas fa-brain text-[#C9A227]"></i></div>
    </div>
"""

footer_css = """
    .footer-strip {
        position: absolute; bottom: 0; left: 80px; right: 0; height: 30px; background: white; border-top: 1px solid #f1f5f9; display: flex; justify-content: space-between; align-items: center; padding: 0 40px; z-index: 90;
    }
    .footer-text { font-family: 'Inter', sans-serif; font-size: 10px; color: #94a3b8; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
    .footer-logo { font-size: 12px; color: #cbd5e1; }
"""

base_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_deck\slides"

for i in range(2, 30):
    filename = f"slide_{i}.html"
    filepath = os.path.join(base_dir, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Add CSS
        if ".footer-strip" not in content:
            content = content.replace("</style>", f"{footer_css}\n</style>")
            
        # Add HTML
        if "footer-strip" not in content:
            content = content.replace("</body>", f"{footer_html}\n</body>")
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated {filename}")
