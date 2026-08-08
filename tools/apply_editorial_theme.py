import os
import re
from bs4 import BeautifulSoup

slides_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

editorial_style_css = """
    /* =========================================================
       EMPIRE & EDITORIAL THEME (DESIGNER GENERATED AESTHETIC)
       ========================================================= */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400&family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        --bg-color: #F8F8F4;        /* Warm cream */
        --surface-color: #FFFFFF;   /* Crisp white */
        --surface-low: #F0F0EA;     /* Muted cream */
        --text-headline: #0A192F;   /* Deep Navy */
        --text-body: #334155;       /* Slate */
        --accent-gold: #C9A227;     /* Sophisticated Muted Gold */
        --accent-emerald: #064E3B;  /* Deep Emerald */
        --border-ghost: rgba(10, 25, 47, 0.08); /* 8% opacity navy */
    }

    body {
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif !important;
        background-color: var(--bg-color) !important;
        color: var(--text-body) !important;
        overflow: hidden;
    }

    /* Main Container overrides */
    .slide-container {
        background-color: var(--bg-color) !important;
        border: none !important;
    }

    /* Typography Overrides */
    h1, h2, h3, h4, h5,
    .main-title, .phase-title, .box-title, .step-title, 
    .card-content h3, .quote-text, .footer-text, .cta-headline, .reality-box {
        font-family: 'Playfair Display', serif !important;
        color: var(--text-headline) !important;
        letter-spacing: -0.02em !important;
    }

    .main-title {
        font-size: 56px !important;
        font-weight: 700 !important;
        line-height: 1.1 !important;
        margin-bottom: 12px !important;
        color: var(--text-headline) !important;
    }

    .sub-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: var(--accent-gold) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.15em !important;
        margin-bottom: 40px !important;
        border-bottom: 1px solid var(--accent-gold);
        display: inline-block;
        padding-bottom: 4px;
    }

    /* Destroy "AI-looking" generic background blob elements */
    .header-bg, .accent-bar, .bg-element, .bg-gradient-accent, .bg-shield-icon {
        display: none !important;
    }

    /* Zero-Radius, Sharp, High-End Surface Cards */
    .value-card, .phase-card, .cost-card, .pain-card, .box, 
    .pipeline-stage, .step-card, .shield-container, .pilot-card {
        border-radius: 0px !important;
        border: 1px solid var(--border-ghost) !important;
        background-color: var(--surface-color) !important;
        /* Ambient depth shadow instead of harsh drop shadow */
        box-shadow: 0 10px 40px -10px rgba(10, 25, 47, 0.03) !important;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
        overflow: visible !important;
    }
    
    .value-card:hover, .phase-card:hover, .cost-card:hover, .pain-card:hover, 
    .box:hover, .pipeline-stage:hover, .step-card:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 20px 40px -10px rgba(10, 25, 47, 0.08) !important;
        border-color: var(--accent-gold) !important;
    }
    
    .value-card::after { display: none !important; } /* Remove decorative corner */

    /* Badges */
    .floating-badge, .problem-badge, .badge-cost, .fail-badge, 
    .model-badge, .value-badge, .page-badge {
        position: absolute !important;
        top: 40px !important;
        right: 60px !important;
        background-color: transparent !important;
        color: var(--accent-gold) !important;
        border: 1px solid var(--accent-gold) !important;
        border-radius: 0 !important;
        padding: 6px 16px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        letter-spacing: 0.15em !important;
        text-transform: uppercase !important;
        box-shadow: none !important;
    }

    /* Content Area Positioning */
    .content-wrapper {
        padding: 60px 80px !important;
        z-index: 10 !important;
    }

    /* Icons unification */
    .icon-box, .icon-circle, .channel-icon, .stage-icon-circle, 
    .check-icon, .stat-icon, .phase-icon {
        background-color: var(--surface-low) !important;
        color: var(--text-headline) !important;
        border-radius: 0 !important;
        border: 1px solid var(--border-ghost) !important;
        box-shadow: none !important;
    }

    /* Footers and Quote Highlights (Dark Navy Blocks) */
    .footer-quote, .footer-message, .bottom-statement, .cta-box, .footer-highlight, .pilot-card {
        background-color: var(--text-headline) !important;
        color: var(--bg-color) !important;
        border-radius: 0 !important;
        border: none !important;
        box-shadow: 0 20px 40px -10px rgba(10,25,47,0.1) !important;
    }
    
    .footer-quote p, .footer-message p, .bottom-statement p, .cta-box p, .footer-highlight p {
        color: var(--bg-color) !important;
    }

    .highlight-text, .highlight-accent {
        color: var(--accent-gold) !important;
        text-decoration: none !important;
        font-style: italic !important;
    }

    /* Specific element tweaks */
    .connector-arrow::after, .arrow-connector::after {
        border-left-color: var(--text-headline) !important;
    }
    .connector-arrow, .arrow-connector, .timeline-line, .connection-line {
        background: var(--text-headline) !important;
        height: 1px !important;
    }

    /* Matrix/Table */
    .pain-card.highlight {
        border-left: 2px solid var(--accent-gold) !important;
        background: var(--surface-color) !important;
    }
    .table-header { border-bottom: 1px solid var(--text-headline) !important; }
    .table-row {
        border-bottom: 1px solid var(--border-ghost) !important;
        border-left: none !important; border-right: none !important; border-top: none !important;
        box-shadow: none !important;
    }
    .table-row:hover {
        border-left: 2px solid var(--accent-gold) !important;
        transform: translateX(8px) !important;
    }
    .reality-box {
        background-color: transparent !important;
        color: var(--text-headline) !important;
        border: 1px solid var(--text-headline) !important;
        border-radius: 0 !important;
    }

    /* E-charts overrides (where possible) */
    div[id*="Chart"] {
        mix-blend-mode: multiply !important;
    }

    /* Other Fixes */
    .box-left, .box-right { background-color: var(--surface-color) !important; border-color: var(--border-ghost) !important; }
    .skill-item { background: var(--surface-low) !important; border-radius: 0 !important; border: 1px solid var(--border-ghost) !important; }
    .step-number { border-radius: 0 !important; background-color: var(--text-headline) !important; color: var(--accent-gold) !important; border: 1px solid var(--accent-gold) !important; }
    .check-badge { background-color: var(--accent-gold) !important; color: var(--text-headline) !important; border-radius: 0 !important; }
    .gap-label { background: transparent !important; color: var(--text-headline) !important; border: 1px dotted var(--text-headline) !important; border-radius: 0 !important; }
    .phase-header { background-color: var(--surface-low) !important; color: var(--text-headline) !important; border-bottom: 1px solid var(--border-ghost) !important; }
    .week-badge { background-color: var(--text-headline) !important; color: var(--accent-gold) !important; border-radius: 0 !important; }
    .pilot-header { color: var(--bg-color) !important; border-bottom-color: rgba(255,255,255,0.1) !important; }
    .stat-value { color: var(--bg-color) !important; }
    .check-item { border-left-color: var(--accent-gold) !important; border-radius: 0 !important; border: 1px solid var(--border-ghost) !important; }
"""

def update_slides():
    for filename in os.listdir(slides_dir):
        if not filename.endswith('.html'):
            continue
            
        filepath = os.path.join(slides_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check if the style block already exists
        existing_style = soup.find(id='editorial-theme-styles')
        if existing_style:
            existing_style.decompose()
            
        # Add new styling to <head>
        head = soup.find('head')
        if head:
            style_tag = soup.new_tag('style', id='editorial-theme-styles')
            style_tag.string = editorial_style_css
            head.append(style_tag)
            
        # Write updated content back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
    print(f"Successfully applied the Empire & Editorial aesthetic to {len([f for f in os.listdir(slides_dir) if f.endswith('.html')])} slides.")

if __name__ == "__main__":
    update_slides()
