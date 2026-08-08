import os
import re
from bs4 import BeautifulSoup

slides_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

# Additional CSS to append to the existing #editorial-theme-styles
additional_fixes = """
    /* =========================================================
       CRITICAL ALIGNMENT & CLIPPING FIXES
       ========================================================= */
       
    /* 1. Force Header margins down to reclaim vertical space */
    .header-section {
        margin-bottom: 20px !important;
    }

    /* 2. Fix Absolute Positioned Arrows breaking outside containers */
    .arrow-connector, .arrow-separator {
        position: static !important;
        transform: none !important;
        margin: auto 0 !important;
        font-size: 20px !important;
        left: auto !important;
        right: auto !important;
        top: auto !important;
    }
    
    /* 3. Hide the hard-coded timeline line which overlaps cards incorrectly */
    .timeline-line {
        display: none !important;
    }

    /* 4. Tightly compact Icon Circles to prevent vertical clipping */
    .icon-circle {
        margin-bottom: 8px !important;
        margin-top: 0 !important;
        width: 48px !important;
        height: 48px !important;
        font-size: 20px !important;
    }

    /* 5. Compact specific containers */
    .timeline-wrapper, .steps-container {
        margin-bottom: 10px !important;
        margin-top: 0 !important;
        align-items: center !important;
    }

    /* 6. Fix Slide 10's massive CTA Box */
    .cta-box {
        padding: 20px 30px !important;
    }
    .cta-headline {
        font-size: 20px !important;
        margin-bottom: 8px !important;
    }
    .cta-subtext, .cta-box p {
        font-size: 14px !important;
    }
    
    /* 7. Ensure Phase Body doesn't artificially stretch */
    .phase-body {
        min-height: 0 !important;
        padding: 12px 16px !important;
        gap: 8px !important;
    }
    .metric-box {
        padding: 8px 12px !important;
    }
    
    /* 8. Slide 8 Phase Card tweaks */
    .phase-card {
        width: 280px !important;
    }
    
    /* 9. Overall Content Wrapper safe-guard */
    .content-wrapper {
        justify-content: flex-start !important;
        gap: 10px !important;
    }

    .footer-highlight {
        padding: 12px 20px !important;
    }
    .highlight-icon {
        font-size: 24px !important;
    }
    .highlight-text {
        font-size: 18px !important;
    }
"""

def apply_fixes():
    count = 0
    for filename in os.listdir(slides_dir):
        if not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(slides_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find the style block we injected
        style_block = soup.find(id='editorial-theme-styles')
        if style_block:
            # Check if fixes already applied to prevent duplicate appends
            if "CRITICAL ALIGNMENT & CLIPPING FIXES" not in style_block.string:
                style_block.string += additional_fixes
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                count += 1
            
    print(f"Successfully applied absolute positioning and clipping fixes to {count} slides.")

if __name__ == "__main__":
    apply_fixes()
