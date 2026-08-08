import os
from bs4 import BeautifulSoup

slides_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

def patch_slide_1():
    filepath = os.path.join(slides_dir, 'slide_1.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    style_tag = soup.find(id='editorial-theme-styles')
    if style_tag:
        if "/* Slide 1 Specific Overrides */" not in style_tag.string:
            style_tag.string += """
                /* Slide 1 Specific Overrides */
                .content-wrapper {
                    justify-content: center !important; /* Center the title slide vertically */
                    align-items: center !important;     /* Center horizontally */
                    text-align: center !important;
                    gap: 30px !important;
                }
                .header-section {
                    margin-bottom: 20px !important;
                    margin-top: 40px !important;
                    text-align: center !important;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                .main-title {
                    font-size: 60px !important; /* Re-enlarge for title slide impact */
                    margin-bottom: 24px !important;
                    line-height: 1.2 !important;
                    max-width: 900px;
                }
                .sub-title {
                    font-size: 20px !important;
                }
                .pipeline-container {
                    margin-top: 20px !important;
                    margin-bottom: auto !important;
                    gap: 30px !important;
                }
                .pipeline-step {
                    width: 300px !important;
                    padding: 30px 20px !important;
                    align-items: center !important;
                    text-align: center !important;
                }
                /* Statically size the arrows so they don't break flex layout */
                .connector-arrow {
                    height: 2px !important;
                    width: 60px !important;
                    flex: none !important;
                    margin: 0 !important;
                }
                /* Title slide footer */
                .footer-values {
                    display: flex !important;
                    gap: 60px !important;
                    justify-content: center !important;
                    padding-top: 40px !important;
                    padding-bottom: 20px !important;
                    border-top: 1px solid var(--border-ghost) !important;
                    width: 100% !important;
                }
                .value-item {
                    display: flex !important;
                    align-items: center !important;
                    gap: 12px !important;
                }
                .value-text {
                    font-family: 'Playfair Display', serif !important;
                    font-size: 20px !important;
                    color: var(--text-headline) !important;
                    font-weight: 600 !important;
                }
                /* Hide any broken spans */
                .sub-title strong { font-weight: normal !important; }
            """
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("Patched Slide 1")

def patch_slide_10():
    filepath = os.path.join(slides_dir, 'slide_10.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    style_tag = soup.find(id='editorial-theme-styles')
    if style_tag:
        if "/* Slide 10 Specific Overrides (Fix Number Clipping) */" not in style_tag.string:
            style_tag.string += """
                /* Slide 10 Specific Overrides (Fix Number Clipping) */
                .step-card {
                    overflow: visible !important; /* CRITICAL: STOP NUMBERS FROM BEING CLIPPED */
                    position: relative !important;
                    padding-top: 40px !important; /* Give extra inside space for the numbers */
                }
                .step-number {
                    position: absolute !important;
                    top: -20px !important; /* Pop out of the top border */
                    left: 50% !important;
                    transform: translateX(-50%) !important;
                    z-index: 20 !important;
                    
                    /* Styling the number circle */
                    border: 2px solid var(--surface-color) !important; 
                    width: 40px !important;
                    height: 40px !important;
                    display: flex !important;
                    align-items: center !important;
                    justify-content: center !important;
                    background-color: var(--text-headline) !important;
                    color: var(--accent-gold) !important;
                    font-size: 16px !important;
                    border-radius: 0 !important; /* Sharp corner aesthetic */
                }
                .icon-circle {
                    margin-top: 0 !important;
                }
                .cta-box {
                    margin-top: auto !important; /* Push to absolute bottom */
                }
            """
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("Patched Slide 10")

if __name__ == '__main__':
    patch_slide_1()
    patch_slide_10()
