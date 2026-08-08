import os
import re
from bs4 import BeautifulSoup

slides_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

fixed_editorial_style_css = """
    /* =========================================================
       EMPIRE & EDITORIAL THEME - ALIGNMENT FIXED
       ========================================================= */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --bg-color: #F8F8F4;        /* Warm cream */
        --surface-color: #FFFFFF;   /* Crisp white */
        --surface-low: #F0F0EA;     /* Muted cream */
        --text-headline: #0A192F;   /* Deep Navy */
        --text-body: #334155;       /* Slate */
        --accent-gold: #C9A227;     /* Sophisticated Muted Gold */
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
        box-sizing: border-box !important;
    }

    /* Typography Overrides */
    h1, h2, h3, h4, h5,
    .main-title, .phase-title, .box-title, .step-title, 
    .card-content h3, .quote-text, .footer-text, .cta-headline, .reality-box {
        font-family: 'Playfair Display', serif !important;
        color: var(--text-headline) !important;
        letter-spacing: -0.01em !important;
    }

    .main-title {
        font-size: 42px !important; /* Scaled down from 56px to avoid overlap */
        font-weight: 800 !important;
        line-height: 1.1 !important;
        margin-bottom: 8px !important;
        color: var(--text-headline) !important;
    }

    .sub-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: var(--accent-gold) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 24px !important; /* Scaled down */
        border-bottom: 1px solid var(--accent-gold);
        display: inline-block;
        padding-bottom: 4px;
    }

    /* Destroy "AI-looking" generic background blob elements */
    .header-bg, .accent-bar, .bg-element, .bg-gradient-accent, .bg-shield-icon {
        display: none !important;
    }

    /* General Surface Cards Fixes */
    .value-card, .phase-card, .cost-card, .pain-card, .box, 
    .pipeline-stage, .step-card, .shield-container, .pilot-card {
        border-radius: 0px !important;
        border: 1px solid var(--border-ghost) !important;
        background-color: var(--surface-color) !important;
        box-shadow: 0 4px 15px -5px rgba(10, 25, 47, 0.03) !important; /* Softer base shadow */
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        overflow: hidden !important; /* Prevent child bleeds */
        box-sizing: border-box !important;
    }
    
    .value-card:hover, .phase-card:hover, .cost-card:hover, .pain-card:hover, 
    .box:hover, .pipeline-stage:hover, .step-card:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px -10px rgba(10, 25, 47, 0.08) !important;
        border-color: var(--accent-gold) !important;
    }
    
    .value-card::after { display: none !important; }

    /* Badges alignment */
    .floating-badge, .problem-badge, .badge-cost, .fail-badge, 
    .model-badge, .value-badge, .page-badge {
        position: absolute !important;
        top: 30px !important;
        right: 40px !important;
        background-color: transparent !important;
        color: var(--accent-gold) !important;
        border: 1px solid var(--accent-gold) !important;
        border-radius: 0 !important;
        padding: 4px 12px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 600 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        box-shadow: none !important;
        z-index: 50 !important;
    }

    /* Fix Master Container Paddings so they don't force vertical overflow */
    .content-wrapper {
        padding: 30px 40px !important;
        z-index: 10 !important;
        height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        box-sizing: border-box !important;
    }

    /* Scale Down Footer elements which consume massive vertical space */
    .footer-quote, .footer-message, .bottom-statement, .cta-box, .footer-highlight, .pilot-card {
        background-color: var(--text-headline) !important;
        color: var(--bg-color) !important;
        border-radius: 0 !important;
        border: none !important;
        padding: 16px 24px !important; /* Scaled Down */
        margin-top: auto !important; /* Pushes to bottom natively */
        box-sizing: border-box !important;
    }
    
    .footer-quote p, .footer-message p, .bottom-statement p, .cta-box p, .footer-highlight p,
    .footer-text, .statement-text {
        font-size: 18px !important; /* Scaled down from 24px+ */
        margin: 0 !important;
        color: var(--bg-color) !important;
    }

    .highlight-text, .highlight-accent {
        color: var(--accent-gold) !important;
        text-decoration: none !important;
        font-style: italic !important;
    }

    /* Icon resizing globally for compactness */
    .icon-box, .channel-icon {
        width: 48px !important;
        height: 48px !important;
        font-size: 20px !important;
        flex-shrink: 0 !important;
    }
    .icon-circle, .stage-icon-circle {
        width: 56px !important;
        height: 56px !important;
        font-size: 24px !important;
        margin-bottom: 12px !important;
    }
    .icon-box, .icon-circle, .channel-icon, .stage-icon-circle, .check-icon, .stat-icon, .phase-icon {
        background-color: var(--surface-low) !important;
        color: var(--text-headline) !important;
        border-radius: 0 !important;
        border: 1px solid var(--border-ghost) !important;
        box-shadow: none !important;
    }

    /* Connectors & Lines */
    .connector-arrow::after, .arrow-connector::after {
        border-left-color: var(--text-headline) !important;
    }
    .connector-arrow, .arrow-connector, .timeline-line, .connection-line {
        background: var(--text-headline) !important;
        height: 1px !important;
        top: auto !important;
    }
    .arrow-separator {
        color: var(--text-headline) !important;
    }

    /* -------------------------------------------
       SLIDE-SPECIFIC FIXES
       ------------------------------------------- */
    
    /* SLIDE 1 (Pipeline) */
    .pipeline-container { margin-bottom: 20px !important; gap: 20px !important; justify-content: center !important; }
    .pipeline-step { width: 260px !important; padding: 20px !important; }

    /* SLIDE 2 & 3 (Grids & Charts) */
    .main-grid { gap: 30px !important; flex: 1 !important; min-height: 0 !important; overflow: hidden !important;}
    .pain-points-container, .cost-cards { gap: 12px !important; justify-content: center !important; }
    .pain-card, .cost-card { padding: 14px 20px !important; gap: 16px !important; }
    .card-content h3 { font-size: 18px !important; margin-bottom: 4px !important;}
    .card-content p { font-size: 14px !important; line-height: 1.3 !important;}
    .chart-container, .chart-wrapper { height: 100% !important; max-height: 380px !important; }
    .chart-center-text h2 { font-size: 28px !important; margin-top: -10px !important;}

    /* SLIDE 4 (Comparison Table) */
    .table-header { grid-template-columns: 240px 1fr 1fr !important; padding: 12px 24px !important; }
    .table-row { grid-template-columns: 240px 1fr 1fr !important; padding: 16px 24px !important; }
    .col-header { font-size: 15px !important; }
    .channel-name { font-size: 16px !important; }
    .promise-text { font-size: 15px !important; }
    .reality-box { padding: 6px 12px !important; font-size: 14px !important; }

    /* SLIDE 5 (Diagram Gap) */
    .diagram-container { padding-bottom: 20px !important; gap: 30px !important; }
    .box { width: 340px !important; padding: 20px !important; height: auto !important; min-height: 280px !important; }
    .box-title { font-size: 20px !important; margin-bottom: 16px !important; }
    .skill-item { padding: 8px 12px !important; font-size: 14px !important; }
    .broken-link-icon { width: 70px !important; height: 70px !important; font-size: 40px !important; }

    /* SLIDE 6 (Demand Flow) */
    .pipeline-wrapper { gap: 10px !important; margin-bottom: 20px !important; }
    .pipeline-stage { width: 280px !important; height: auto !important; padding: 24px 20px !important; min-height: 240px !important; }
    .stage-label { font-size: 18px !important; }
    .stage-desc { font-size: 14px !important; }
    .stage-tag { top: 0 !important; left: 0 !important; border-radius: 0 !important; padding: 4px 8px !important; }
    
    /* SLIDE 7 (WIIFM Grid) */
    .value-grid { gap: 20px !important; margin-bottom: 20px !important; }
    .value-card { padding: 20px !important; gap: 16px !important; }

    /* SLIDE 8 (Execution Timeline) */
    .timeline-wrapper { gap: 20px !important; margin-top: 10px !important; padding: 0 !important; justify-content: center !important;}
    .phase-card { width: 300px !important; }
    .phase-header { padding: 12px 16px !important; font-size: 14px !important; }
    .phase-body { padding: 16px !important; min-height: 140px !important; }
    .phase-title { font-size: 18px !important; }
    .phase-desc { font-size: 13px !important; margin-top: 4px !important; }
    .metric-box { padding: 10px 16px !important; }
    .metric-value { font-size: 14px !important; }
    .arrow-1, .arrow-2 { font-size: 18px !important; } /* Center arrows manually scaled */

    /* SLIDE 9 (Risk Shield) */
    .risk-column { overflow: visible !important; }
    .shield-container { padding: 20px !important; }
    .checklist-grid { gap: 12px !important; }
    .check-item { padding: 12px 16px !important; }
    .check-text { font-size: 15px !important; }
    .pilot-card { padding: 24px !important; }
    .pilot-header { font-size: 18px !important; margin-bottom: 20px !important; padding-bottom: 12px !important; }
    .pilot-stat { margin-bottom: 20px !important; }
    .stat-value { font-size: 28px !important; }

    /* SLIDE 10 (Next Steps) */
    .steps-container { margin-bottom: 30px !important; gap: 20px !important; }
    .step-card { padding: 24px 20px !important; }
    .step-title { font-size: 20px !important; margin-bottom: 8px !important; }
    .step-desc { font-size: 14px !important; }
    .cta-headline { font-size: 24px !important; margin-bottom: 10px !important; line-height: 1.3 !important; }
    .cta-subtext { font-size: 16px !important; }

    /* Misc Overrides */
    .box-left, .box-right { background-color: var(--surface-color) !important; border-color: var(--border-ghost) !important; }
    .skill-item { background: var(--surface-low) !important; border-radius: 0 !important; border: 1px solid var(--border-ghost) !important; }
    .step-number { border-radius: 0 !important; background-color: var(--text-headline) !important; color: var(--accent-gold) !important; border: 1px solid var(--accent-gold) !important; width: 32px !important; height: 32px !important; font-size: 16px !important; top: -16px !important;}
    .check-badge { background-color: var(--accent-gold) !important; color: var(--text-headline) !important; border-radius: 0 !important; width: 24px !important; height: 24px !important; font-size: 14px !important; }
    .gap-label { background: transparent !important; color: var(--text-headline) !important; border: 1px solid var(--text-headline) !important; border-radius: 0 !important; padding: 4px 10px !important; }
    .phase-header { background-color: var(--surface-low) !important; color: var(--text-headline) !important; border-bottom: 1px solid var(--border-ghost) !important; }
    .week-badge { background-color: var(--text-headline) !important; color: var(--accent-gold) !important; border-radius: 0 !important; font-size: 10px !important; }
"""

def fix_all_alignments():
    count = 0
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
            style_tag.string = fixed_editorial_style_css
            head.append(style_tag)
            
        # Additionally, let's inject a wrapper fix for Echarts so they don't break flex layouts
        for chart_wrapper in soup.select('.chart-wrapper, .chart-container'):
            # Just ensure inline styles don't conflict excessively
            pass

        # Write updated content back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            count += 1
            
    print(f"Successfully applied precise alignment fixes to {count} slides.")

if __name__ == "__main__":
    fix_all_alignments()
